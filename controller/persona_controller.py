from flask import request, jsonify
import server, db
from entity.persona_entity import  Persona



def persona_create():
    json = request.json
    persona = Persona(**json)
    db.session.add(persona)
    db.session.commit()
    return jsonify(
        _Status = "success",
        data = json
    )
def persona_read(id):
    persona = db.session.query(Persona).get(id)
    return jsonify(
        status = "success",
        data = persona.to_dict()
    )

def personas_update(id):
    json = request.json
    persona = db.session.query(Persona).get(id)
    for key, value in json.items():
        if hasattr(persona, key):
            setattr(persona, key, value)
    db.session.commit()
    return jsonify(
        status="success",
        data = persona.to_dict()
    )
    
def persona_delete(id):
    persona = db.session.query(Persona).get(id)
    db.session.delete(persona)
    db.session.commit()
    return jsonify(
        status ="success",
        data = persona.to_dict()
    )