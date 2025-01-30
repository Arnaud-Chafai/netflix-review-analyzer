from flask import Flask, request, jsonify, render_template
import pandas as pd
import random

app = Flask(__name__)

# Cargar el archivo CSV
df = pd.read_csv("C:\\Users\\Usuario\\Desktop\\Netflix\\Raw_data\\reseñas_tablon_final.csv", index_col=0)

# Ruta para servir el frontend
@app.route('/')
def index():
    return render_template('front.html')

# Ruta para el endpoint de recomendación
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    movie1 = data.get("movie1")
    movie2 = data.get("movie2")
    current_type = data.get("type")  # 'movie' o 'series'

    # Lógica aleatoria para recomendar una película o serie
    random_index = random.randint(0, len(df) - 1)
    random_title = df.iloc[random_index]["title"]

    # Filtrar los comentarios relacionados con el título recomendado
    comentarios = df[df["title"] == random_title][["title_comment", "comment"]]

    # Verificar si hay comentarios disponibles
    if len(comentarios) > 0:
        random_comment_index = random.randint(0, len(comentarios) - 1)
        selected_comment = comentarios.iloc[random_comment_index]
        title_comment = selected_comment["title_comment"]
        comment = selected_comment["comment"]
    else:
        title_comment = "No comments available"
        comment = "No additional details for this recommendation."

    return jsonify({
        "recommendation": random_title,
        "review": {
            "title_comment": title_comment,
            "comment": comment
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
