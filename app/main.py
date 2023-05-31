from flask import request, jsonify
import pandas as pd

from app import app

data_file = "vibra_challenge.csv"

@app.route('/search', methods=['GET'])
def search():
    name = request.args.get('name')
    city = request.args.get('city')
    quantity = request.args.get('quantity')

    # Leer el archivo CSV
    df = pd.read_csv(data_file)

    # Filtrar los registros basados en los parámetros de búsqueda
    if name:
        df = df[df['Name'] == name]
    if city:
        df = df[df['City'] == city]
    if quantity:
        df = df.head(int(quantity))

    # Convertir los resultados a formato JSON
    results = df.to_json(orient='records')

    return results


if __name__ == '__main__':
    app.run()
