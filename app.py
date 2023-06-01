from flask import Flask, request
from flask_cors import CORS
from db import __init__, client
from bson.objectid import ObjectId

# Starting application
app = Flask(__name__)
CORS(app)

# Schema connection
IC = client.iniciacaoCientifica


# Professors route
@app.route('/professors', methods=["GET"])
def get_professors():
    try:
        professors = IC.professor_collection.find()
        response = [{item: professor[item] for item in professor if item != '_id'} for professor in professors]
    except:
        response = {"message": "Falha ao buscar os professores"}

    return response


@app.route('/professors', methods=["POST"])
def insert_professors():
    new_professor = request.get_json()

    try:
        IC.professor_collection.insert_one(new_professor)
        response = {"message": "Professor cadastrado com sucesso!"}
    except:
        response = {"message": "Falha ao cadastrar o professor"}

    return response


@app.route('/professors/<id>', methods=["GET"])
def get_one_professor_by_id(id):
    _id = ObjectId(id)

    try:
        professor = IC.professor_collection.find_one({"_id": _id})

        response = {item: professor[item] for item in professor if item != '_id'}
    except:
        response = {"message": f"Falha ao buscar professor id {id}!"}

    return response


@app.route('/professors/<id>', methods=["PUT"])
def update_professor(id):
    _id = ObjectId(id)

    update = request.get_json()

    try:
        IC.professor_collection.update_one({"_id": _id}, {"$set": update})
        response = {"message": f"Professor {id} atualizado com sucesso!"}
    except:
        response = {"message": f"Falha ao atualizar professor id {id}"}

    return response


@app.route('/professors/<id>', methods=["DELETE"])
def delete_professor(id):
    _id = ObjectId(id)

    try:
        IC.professor_collection.delete_one({"_id": _id})
        response = {"message": f"Professor {id} deletado com sucesso!"}
    except:
        response = {"message": f"Falha ao deletar o professor id {id}"}

    return response


# Schema course
@app.route('/courses', methods=["POST"])
def insert_courses():
    new_courses = request.get_json()

    try:
        IC.courses_collection.insert_one(new_courses)
        response = {"message": "Curso adicionado com sucesso!"}
    except:
        response = {"message": "Falha ao cadastrar o curso"}

    return response


@app.route('/courses', methods=["GET"])
def get_courses():
    try:
        courses = IC.courses_collection.find()
        response = [{item: course[item] for item in course if item != "_id"} for course in courses]
    except:
        response = {"message": "Falha ao buscar os cursos"}

    return response


@app.route('/courses/<id>', methods=["GET"])
def get_one_courses_by_id(id):
    _id = ObjectId(id)

    try:
        course = IC.courses_collection.find_one({"_id": _id})

        response = {item: course[item] for item in course if item != "_id"}
    except:
        response = {"message": f"Falha ao buscar curso id {id}"}

    return response


@app.route('/courses/<id>', methods=["PUT"])
def update_courses(id):
    _id = ObjectId(id)

    update = request.get_json()

    try:
        IC.courses_collection.update_one({"_id": _id}, {"$set": update})
        response = {"message": f"Course {id} atualizado com sucesso!"}
    except:
        response = {"message": f"Falha ao atualizar course {id}"}

    return response


@app.route('/courses/<id>', methods=["DELETE"])
def delete_course(id):
    _id = ObjectId(id)

    try:
        IC.courses_collection.delete_one({"_id": _id})
        response = {"message": f"Course id {id} deletado com sucesso!"}
    except:
        response = {"message": f"Falha ao deletar o course id {id}"}

    return response


# Schema classes
@app.route('/classes', methods=["POST"])
def insert_classe():
    new_classes = request.get_json()

    try:
        IC.classes_collection.insert_one(new_classes)
        response = {"message": "Classe cadastrada com sucesso!"}
    except:
        response = {"message": "Falha ao cadastrar a classe"}

    return response


@app.route('/classes', methods=["GET"])
def get_classes():
    try:
        classes = IC.classes_collection.find()
        response = [{item: classe[item] for item in classe if item != "_id"} for classe in classes]
    except:
        response = {"message": "Falha ao buscar classes"}

    return response


@app.route('/classes/<id>', methods=["GET"])
def get_one_classe_by_id(id):
    _id = ObjectId(id)

    try:
        classe = IC.classes_collection.find_one({"_id": _id})
        response = {item: classe[item] for item in classe if item != "_id"}
    except:
        response = {"message": f"Falha oa buscar a classe id {id}"}

    return response


@app.route('/classes/<id>', methods=["PUT"])
def update_classe(id):
    _id = ObjectId(id)
    update = request.get_json()

    try:
        IC.classes_collection.update_one({"_id": _id}, {"$set": update})
        response = {"message": f"Classes id {id} atualizada com sucesso!"}
    except:
        response = {"message": f"Falha ao atualizar classes id {id}"}

    return response


@app.route('/classes/<id>', methods=["DELETE"])
def delete_classe(id):
    _id = ObjectId(id)

    try:
        IC.classes_collection.delete_one({"_id": _id})
        response = {"message": f"Classe id {id} deletada com sucesso!"}
    except:
        response = {"message": f"Falha ao deletar calsse id {id}"}

    return response


# Schema subjects
@app.route('/subjects', methods=["POST"])
def insert_subject():
    new_subject = request.get_json()

    try:
        IC.subjects_collection.insert_one(new_subject)
        response = {"message": "Disciplina adicionada com sucesso!"}
    except:
        response = {"message": "Falha ao adicionar disciplina"}

    return response


@app.route('/subjects', methods=["GET"])
def get_subjects():
    try:
        subjects = IC.subjects_collection.find()
        response = [{item: subject[item] for item in subject if item != "_id"} for subject in subjects]
    except:
        response = {"message": "Falha ao buscar as disciplinas"}

    return response


@app.route('/subjects/<id>', methods=["GET"])
def get_one_subject_by_id(id):
    _id = ObjectId(id)

    try:
        subject = IC.subjects_collection.find_one({"_id": _id})
        response = {item: subject[item] for item in subject if item != "_id"}
    except:
        response = {"message": f"Falha ao buscar a disciplina id {id}"}

    return response


@app.route('/subjects/<id>', methods=["PUT"])
def update_subject(id):
    _id = ObjectId(id)
    update = request.get_json()

    try:
        IC.subjects_collection.update_one({"_id": _id}, {"$set": update})
        response = {"message": f"Disciplina id {id} atualizada com sucesso!"}
    except:
        response = {"message": f"Falha ao atualizar a disciplina id {id}"}

    return response


@app.route('/subjects/<id>', methods=["DELETE"])
def delete_subject(id):
    _id = ObjectId(id)

    try:
        IC.subjects_collection.delete_one({"_id": _id})
        response = {"message": f"Disciplina id {id} deletada com sucesso!"}
    except:
        response = {"message": f"Falha ao deletar a disciplina id {id}"}

    return response


# Schema restrictions
@app.route('/restrictions', methods=["POST"])
def insert_restriction():
    new_restriction = request.get_json()

    try:
        IC.restrictions_collection.insert_one(new_restriction)
        response = {"message": "Restrição adicionada com sucesso!"}
    except:
        response = {"message": "Falha ao adcionar a restrição"}

    return response


@app.route('/restrictions', methods=["GET"])
def get_restrictions():
    try:
        restrictions = IC.restrictions_collection.find()
        response = [{item: restriction[item] for item in restriction if item != "_id"} for restriction in restrictions]
    except:
        response = {"message": "Falha ao buscar restrições"}

    return response


@app.route('/restrictions/<id>', methods=["GET"])
def get_one_restriction_by_id(id):
    _id = ObjectId(id)

    try:
        restriction = IC.restrictions_collection.find_one({"_id": _id})
        response = {item: restriction[item] for item in restriction if item != "_id"}
    except:
        response = {"message": f"Falha ao buscar restrição id {id}"}

    return response


@app.route('/restrictions/<id>', methods=["PUT"])
def update_restriction(id):
    _id = ObjectId(id)
    update = request.get_json()

    try:
        IC.restrictions_collection.update_one({"_id": _id}, {"$set": update})
        response = {"message": f"Restrição id {id} atualizada com sucesso!"}
    except:
        response = {"message": f"Falha ao atualizar a restrição id {id}"}

    return response


@app.route('/restrictions/<id>', methods=["DELETE"])
def delete_restriction(id):
    _id = ObjectId(id)

    try:
        IC.restrictions_collection.delete_one({"_id": _id})
        response = {"message": f"Restrição id {id} deletada com sucesso!"}
    except:
        response = {"message": f"Falha ao deletar a restrição id {id}"}

    return response


if __name__ == '__main__':
    app.run(debug=True)
