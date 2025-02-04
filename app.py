from flask import Flask, request, jsonify, render_template
import pandas as pd
import random
import openai
from dotenv import load_dotenv
import os

# Cargar variables de entorno desde .env
load_dotenv()

# Configurar OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
client = openai.OpenAI(api_key=OPENAI_API_KEY)

app = Flask(__name__)

# Cargar el archivo CSV con las reseñas
df = pd.read_csv("C:\\Users\\Arnaud\\Desktop\\Netflix\\Raw_data\\tablon.csv")
print(f"CSV cargado con éxito. Número de filas: {len(df)}")

@app.route('/')
def index():
    print("Renderizando el frontend...")
    return render_template('front.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    print("Solicitud recibida en /recommend")

    data = request.get_json()
    print(f"Datos recibidos: {data}")

    movie1 = data.get("movie1")
    movie2 = data.get("movie2")
    current_type = data.get("type")
    print(f"Tipo actual: {current_type}, Película 1: {movie1}, Película 2: {movie2}")

    # Seleccionar aleatoriamente una película/serie
    random_index = random.randint(0, len(df) - 1)
    random_title = df.iloc[random_index]["title"]
    print(f"Título seleccionado aleatoriamente: {random_title}")

    # Obtener los comentarios relacionados con el título
    comentarios_df = df[df["title"] == random_title]["comment"]
    print(f"Comentarios encontrados para '{random_title}': {len(comentarios_df)}")

    if comentarios_df.empty:
        print("No se encontraron comentarios para este título.")
        return jsonify({
            "recommendation": random_title,
            "review": "No comments available for this recommendation."
        })

    # Unir comentarios en un string
    comentarios = "\n".join(comentarios_df.sample(min(5, len(comentarios_df))).tolist())
    print("Comentarios enviados a OpenAI:")
    print(comentarios)

    try:
        # Solicitar análisis al modelo GPT
        respuesta = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": f"""
Based on the following user comments {comentarios} about the movie or series '{random_title}', provide a concise analysis in this format:

Summary:
 A brief, 2-line overall perception of the movie/series, based on user feedback.


Positive Consensus:
 One sentence summarizing the most common positive feedback.

Negative Consensus:
 One sentence summarizing the most common criticism.


"""
                }
            ]
        )

        # Debug: Verificar la respuesta de OpenAI
        print("Respuesta de OpenAI:")
        print(respuesta)

        # Extraer la respuesta generada
        analysis = respuesta.choices[0].message.content.strip()
        print("Análisis generado por OpenAI:")
        print(analysis)

    except Exception as e:
        print("Error al comunicarse con OpenAI:", e)
        return jsonify({
            "recommendation": random_title,
            "review": f"Error generating review: {str(e)}"
        })

    # Retornar la recomendación y el análisis
    return jsonify({
        "recommendation": random_title,
        "review": analysis
    })

if __name__ == '__main__':
    app.run(debug=True)