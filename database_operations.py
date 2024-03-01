import sqlalchemy
from models import publicaciones  # Asegúrate de que Publish se importe correctamente desde models

def connect_to_database():
    # Define la cadena de conexión a la base de datos
    DATABASE_URL = "postgresql://postgres:M@1122919448@localhost:5432/PostgreSQL15"
    
    # Crea un motor de SQLAlchemy con la codificación especificada
    engine = sqlalchemy.create_engine(DATABASE_URL, client_encoding='utf8')
    
    # Conecta al motor
    connection = engine.connect()
    
    return connection

def fetch_all_publications():  # Corrige el nombre de la función a fetch_all_publications
    try:
        # Obtiene todas las publicaciones
        publications = publicaciones.query.all()  # Usa Publish en lugar de Publicaciones
        
        # Decodifica los datos si son bytes
        decoded_publications = []
        for publication in publications:
            decoded_publication = {}
            for key, value in publication.__dict__.items():
                if isinstance(value, bytes):
                    try:
                        # Intenta decodificar utf-8
                        decoded_value = value.decode('utf-8')
                    except UnicodeDecodeError:
                        # Si falla, intenta decodificar latin1 con reemplazo de errores
                        decoded_value = value.decode('latin1', errors='ignore')
                    decoded_publication[key] = decoded_value
                else:
                    decoded_publication[key] = value
            decoded_publications.append(decoded_publication)
        
        return decoded_publications
    except Exception as e:
        # Manejo de errores
        print("Error fetching publications:", str(e))
        return []

def close_database_connection(connection):
    # Cierra la conexión
    connection.close()
