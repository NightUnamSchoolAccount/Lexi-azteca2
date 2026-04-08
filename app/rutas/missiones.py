from flask import Blueprint, request, jsonify, current_app
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from dotenv import load_dotenv
import os

load_dotenv()

ms_bl = Blueprint('misiones', __name__, url_prefix='/misiones')


DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(DATABASE_URL)

Base = automap_base()
Base.prepare(engine, reflect=True)


#revisar si podemos hacer un hud
@ms_bl.route('/', methods=['POST'])
def agregar_misiones():
    """
    Agregar misiones
    ---
    tags:
      - misiones
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - mission_name
            - mission_type
            - description
            - status
            - xp_drop
          properties:
            mission_name:
              type: string
              example: "Primera misión"
            mission_type:
              type: string
              example: "Primera misión"
            description:
              type: string
              example: "Completa el tutorial"
            status:
              type: string
              enum: [pregunta, completar]
              example: "pregunta"
            xp_drop:
              type: integer
              example: 100
            status:
              type: string
              example: "active"
    responses:
      201:
        description: Misión creada
      400:
        description: Error en datos
    """
    session = current_app.Session()
    try:
        Missions = Base.classes.missiones
        data = request.get_json()
        data.pop('mission_id', None)
        nuevo = Missions(**data)
        session.add(nuevo)
        session.commit()
        result = {col.key: getattr(nuevo, col.key) for col in Missions.__table__.columns}
        return jsonify(result), 201
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 400
    finally:
        session.close()


    

#agregar mision

#lista de misiones



