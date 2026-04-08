from flask import Blueprint, request, jsonify
from app.Handlers.WhatsAppHandler import WhatsAppHandler

wa_bp = Blueprint('whatsapp', __name__, url_prefix='/whatsapp')


@wa_bp.route('/send-template', methods=['POST'])
def send_template():
    """
    Envía un mensaje de plantilla de WhatsApp
    ---
    tags:
      - whatsapp
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - to
            - template_name
          properties:
            to:
              type: string
              example: "525619283816"
            template_name:
              type: string
              example: "hello_world"
            language_code:
              type: string
              example: "en_US"
    responses:
      200:
        description: Mensaje enviado correctamente
      400:
        description: Datos inválidos
      500:
        description: Error al enviar el mensaje
    """
    body = request.get_json()
    to = body.get('to')
    template_name = body.get('template_name')
    language_code = body.get('language_code', 'en_US')

    if not to or not template_name:
        return jsonify({"error": "Los campos 'to' y 'template_name' son requeridos"}), 400

    try:
        handler = WhatsAppHandler()
        result = handler.send_template(to, template_name, language_code)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@wa_bp.route('/send-text', methods=['POST'])
def send_text():
    """
    Envía un mensaje de texto libre de WhatsApp
    ---
    tags:
      - whatsapp
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - to
            - message
          properties:
            to:
              type: string
              example: "525619283816"
            message:
              type: string
              example: "Hola, ¿cómo estás?"
    responses:
      200:
        description: Mensaje enviado correctamente
      400:
        description: Datos inválidos
      500:
        description: Error al enviar el mensaje
    """
    body = request.get_json()
    to = body.get('to')
    message = body.get('message')

    if not to or not message:
        return jsonify({"error": "Los campos 'to' y 'message' son requeridos"}), 400

    try:
        handler = WhatsAppHandler()
        result = handler.send_text(to, message)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@wa_bp.route('/update-token', methods=['POST'])
def update_token():
    """
    Actualiza el token de WhatsApp en el servidor
    ---
    tags:
      - whatsapp
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - token
          properties:
            token:
              type: string
              example: "EAAUV55nEDq0..."
    responses:
      200:
        description: Token actualizado correctamente
      400:
        description: Token no proporcionado
    """
    body = request.get_json()
    token = body.get('token')

    if not token:
        return jsonify({"error": "El campo 'token' es requerido"}), 400

    handler = WhatsAppHandler()
    handler.update_token(token)
    return jsonify({"message": "Token actualizado correctamente"}), 200
