from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import random

app = Flask(__name__)
CORS(app)  # Habilitar CORS

# Cargar el archivo CSV
df = pd.read_csv("C:\\Users\\Usuario\\Desktop\\Netflix\\Raw_data\\reseñas_tablon_final.csv", index_col=0)

@app.route('/recommend', methods=['POST'])
def recommend():
    # Obtener datos enviados desde el frontend
    data = request.get_json()
    movie1 = data.get("movie1")
    movie2 = data.get("movie2")
    current_type = data.get("type")  # 'movie' o 'series'

    # Lógica aleatoria para recomendar una película o serie
    random_index = random.randint(0, len(df) - 1)
    random_title = df.iloc[random_index]["title"]

    return jsonify({
        "recommendation": random_title,
        "summary": f"Recommended {current_type} based on your input: '{movie1}' and '{movie2}'."
    })

if __name__ == '__main__':
    app.run(debug=True)
