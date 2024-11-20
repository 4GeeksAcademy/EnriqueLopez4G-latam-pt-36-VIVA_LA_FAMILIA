"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
#EnriqueLopez4G
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

#primer endpoint solicitado.
@app.route('/members', methods=['GET'])
def handle_hello():
    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()

    return jsonify(members), 200
#------------------------------


#segundo endpoint solicitado
# Primer endpoint (corregido y único)
@app.route('/member/<int:id>', methods=['GET'])
def get_member_by_id(id):
    # Obtener el miembro por su ID viene el decorador y lo atrapo tambein en el def
    member = jackson_family.get_member(id)
    
    if member is None:
        # Si no se encuentra el miembro, retornamos un 404
        return jsonify({"error": "Miembro no localizado"}), 404

    # Si el miembro existe, lo retornamos con un código 200
    return jsonify(member), 200

#---------------------------------------

#tercer endpoint solicitado
@app.route('/member',methods=['POST'])
def addMember():
    newMember = request.get_json()

    # Validación de campos requeridos
    if "first_name" not in newMember or "age" not in newMember or "lucky_numbers" not in newMember:
        return {"error": "Faltan campos en este miembro"}, 400
    
    # Verificación de tipos de datos
    if not isinstance(newMember["age"], int) or not isinstance(newMember["lucky_numbers"], list):
        return {"error": "El tipo de datos no es valido"}, 400
    
    # Llamar al método add_member
    member, status_code = jackson_family.add_member(newMember)
    # Retornar la respuesta y el código de estado adecuado
    return jsonify(member), status_code
#------------------------------------------------

#cuarto endpoint solicitado
#el famoso delete
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    try:
        # Intentar eliminar el miembro
        member = jackson_family.delete_member(id)

        if member is None:
            # Si el miembro no se encuentra, retornar un mensaje de error y un código 404
            return jsonify({"error": "miembro no encontrado"}), 404
        
         # Si el miembro se eliminó correctamente, retornar un diccionario con la clave 'done' y valor True
        return jsonify(
            {
                "done": True
                }
            ), 200
        
        

    except Exception as e:
        # Si ocurre algún error inesperado,devielve el codigo 500 con un mensajito
        return jsonify({"error": "error del server", "message": str(e)}), 500
    
    




#---------------------------------------------------
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
