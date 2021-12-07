from flask import request, jsonify
import server, db
from entity.car_entity import  Car



def car_create():
    json = request.json
    car = Car(**json)
    db.session.add(car)
    db.session.commit()
    return jsonify(
        _Status = "success",
        data = json
    )
def car_read(id):
    car = db.session.query(Car).get(id)
    return jsonify(
        status = "success",
        data = car.to_dict()
    )

def cars_update(id):
    json = request.json
    car = db.session.query(Car).get(id)
    for key, value in json.items():
        if hasattr(car, key):
            setattr(car, key, value)
    db.session.commit()
    return jsonify(
        status="success",
        data = car.to_dict()
    )
    
def car_delete(id):
    car = db.session.query(Car).get(id)
    db.session.delete(car)
    db.session.commit()
    return jsonify(
        status ="success",
        data = car.to_dict()
    )