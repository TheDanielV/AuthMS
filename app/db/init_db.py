from app.db.database import Base, engine
import app.models.domain.auth  # Asegúrate de importar los modelos aquí


# Se inicia labase de datos y de ser el caso crea la tabla
def init_db():
    print("Creando tablas en la base de datos...")
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Error al crear tablas: {e}")
