import os
import csv
from flask import Flask, request, jsonify

app = Flask(__name__)


# Rutas de archivos
csv_path = 'vibra_challenge.csv'

# Construir la ruta completa del archivo CSV
current_dir = os.path.dirname(os.path.abspath(__file__))
csv_path_complete = os.path.join(current_dir, csv_path)


# Ruta para la búsqueda
@app.route('/search', methods=['GET'])
def search():
    # Obtener los parámetros de búsqueda de la URL
    name = request.args.get('name')
    city = request.args.get('city')
    quantity = request.args.get('quantity')

    # Leer y filtrar el archivo CSV
    results = read_and_filter_csv(name, city)

    # Limitar los resultados
    if quantity is not None:
        results = results[:int(quantity)]

    # Formatear los resultados en formato JSON
    formatted_results = format_results(results)

    # Retornar los resultados en formato JSON
    return jsonify(formatted_results)


def read_and_filter_csv(name, city):
    # Leer el archivo CSV
    try:
        with open(csv_path_complete, 'r', encoding='utf-8-sig') as file:
            reader = csv.reader(file)

            # Filtrar los datos
            results = []
            for row in reader:
                row_name = row[1].lower()
                row_city = row[6].lower()

                if (name is None or name.lower() in row_name) and \
                (city is None or city.lower() in row_city):
                    results.append({
                        'id': row[0],
                        'name': row_name,
                        'email': row[3],
                        'gender': row[4],
                        'company': row[5],
                        'city': row_city
                    })
            return results
    except FileNotFoundError:
        print(f'File not found in route {csv_path_complete}')
        return []  # Devuelve una lista vacía si se produce un error al abrir el archivo


def format_results(results):
    formatted_results = []
    for result in results:
        formatted_results.append({
            'id': result['id'],
            'name': result['name'],
            'email': result['email'],
            'gender': result['gender'],
            'company': result['company'],
            'city': result['city']
        })

    return formatted_results


if __name__ == '__main__':
    app.run(debug=True)