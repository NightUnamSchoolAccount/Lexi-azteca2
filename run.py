import os 
API_KEY = os.getenv('API_KEY_IA')  # Asegúrate de que esta variable de entorno esté configurada correctamente
app = create_app()




#main
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5432))    
    app.run(host='0.0.0.0', port=port, debug=True)

  
