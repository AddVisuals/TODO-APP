from flask import Blueprint, jsonify, request
api = Blueprint('api', __name__, url_prefix='/api/v1')


@api.route('/health')
def health():
    return jsonify({"status": "ok"})


@api.route('/todos/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def get_todo(id):
    if request.method == 'GET':
        data = {
            "id": id,
            "title": "Watch CSSE6400 Lecture",
            "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
            "completed": "false",
            "deadline_at": "2023-02-27T00:00:00",
            "created_at": "2023-02-20T00:00:00",
            "updated_at": "2023-02-20T00:00:00"
        }
        return jsonify(data)
    elif request.method == 'PUT':
        content = request.json
        data = {
            "id": id,
            "title": content["title"],
            "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
            "completed": "false",
            "deadline_at": "2023-02-27T00:00:00",
            "created_at": "2023-02-20T00:00:00",
            "updated_at": "2023-02-20T00:00:00"
        }
        return jsonify(data)
    elif request.method == 'DELETE':
        data = {
            "id": id,
            "title": "Join the Richard Thomas fan club",
            "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
            "completed": "false",
            "deadline_at": "2023-02-27T00:00:00",
            "created_at": "2023-02-20T00:00:00",
            "updated_at": "2023-02-20T00:00:00"
        }
        return jsonify(data)



@api.route('/todos', methods=['GET', 'POST'])
def todos():
    if request.method == 'GET':
        completed = request.args.get('completed')
        if completed is None:
            completed = "false"

        window = request.args.get('window')
        if window is None:
            window = "0"
        data = [{
            "id": 1,
            "title": "Watch CSSE6400 Lecture",
            "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
            "completed": completed,
            "window": window,
            "deadline_at": "2023-02-27T00:00:00",
            "created_at": "2023-02-20T00:00:00",
            "updated_at": "2023-02-20T00:00:00"
        },
            {
                "id": 1,
                "title": "Watch CSSE6400 Lecture",
                "description": "Watch the CSSE6400 lecture on ECHO360 for week 1",
                "completed": completed,
                "window": window,
                "deadline_at": "2023-02-27T00:00:00",
                "created_at": "2023-02-20T00:00:00",
                "updated_at": "2023-02-20T00:00:00"
            }]
        return jsonify(data)
    elif request.method == 'POST':
        content = request.json
        print(request.method)
        print(content)
        data = {
            "id": 1,
            "title": content["title"],
            "description": content["description"],
            "completed": content["completed"],
            "deadline_at": content["deadline_at"],
            "created_at": "2023-02-20T00:00:00",
            "updated_at": "2023-02-20T00:00:00"
        }
        return jsonify(data), 201

