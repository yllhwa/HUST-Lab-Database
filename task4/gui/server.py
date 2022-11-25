import math
from flask import Flask, Blueprint, request
from utils import jsonResponse
import database

server = Flask(__name__)
server.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
server.config['JSON_AS_ASCII'] = False
database.db.init_app(server)


@server.route('/')
def index():
    return server.send_static_file('index.html')


api = Blueprint('api', __name__, url_prefix='/api')


@api.route('/test')
def test():
    return jsonResponse(database.getCourseCount(), 200, "success")


@api.route('/Students', methods=['GET', 'POST', 'PUT', 'DELETE'])
def getStudents():
    if request.method == 'GET':
        page = request.args.get('page', 1, type=int)
        size = request.args.get('size', 10, type=int)
        total = database.getStudentCount()
        return jsonResponse({
            # 向上取整
            "pageCount":  math.ceil(total / size),
            "data": database.getStudents(page, size),
            "total": total
        }, 200, "success")
    elif request.method == 'POST':
        data = request.get_json()
        try:
            database.addStudent(data)
            return jsonResponse(None, 200, "success")
        except Exception as e:
            return jsonResponse(None, 500, "something wrong")
    elif request.method == 'PUT':
        data = request.get_json()
        try:
            database.updateStudent(data)
            return jsonResponse(None, 200, "success")
        except Exception as e:
            return jsonResponse(None, 500, "something wrong")
    elif request.method == 'DELETE':
        data = request.get_json()
        try:
            database.deleteStudent(data)
            return jsonResponse(None, 200, "success")
        except Exception as e:
            return jsonResponse(None, 500, "something wrong")


@api.route('/Courses', methods=['GET', 'POST', 'PUT', 'DELETE'])
def getCourses():
    if request.method == 'GET':
        page = request.args.get('page', 1, type=int)
        size = request.args.get('size', 10, type=int)
        total = database.getCourseCount()
        return jsonResponse({
            # 向上取整
            "pageCount":  math.ceil(total / size),
            "data": database.getCourses(page, size),
            "total": total
        }, 200, "success")
    elif request.method == 'POST':
        data = request.get_json()
        try:
            database.addCourse(data)
            return jsonResponse(None, 200, "success")
        except Exception as e:
            return jsonResponse(None, 500, "something wrong")
    elif request.method == 'PUT':
        data = request.get_json()
        try:
            database.updateCourse(data)
            return jsonResponse(None, 200, "success")
        except Exception as e:
            return jsonResponse(None, 500, "something wrong")
    elif request.method == 'DELETE':
        data = request.get_json()
        try:
            database.deleteCourse(data)
            return jsonResponse(None, 200, "success")
        except Exception as e:
            return jsonResponse(None, 500, "something wrong")


@api.route('/SCs', methods=['GET', 'POST', 'PUT', 'DELETE'])
def getSCs():
    if request.method == 'GET':
        page = request.args.get('page', 1, type=int)
        size = request.args.get('size', 10, type=int)
        total = database.getSCCount()
        return jsonResponse({
            # 向上取整
            "pageCount":  math.ceil(total / size),
            "data": database.getSCs(page, size),
            "total": total
        }, 200, "success")
    elif request.method == 'POST':
        data = request.get_json()
        try:
            database.addSC(data)
            return jsonResponse(None, 200, "success")
        except Exception as e:
            return jsonResponse(None, 500, "something wrong")
    elif request.method == 'PUT':
        data = request.get_json()
        try:
            database.updateSC(data)
            return jsonResponse(None, 200, "success")
        except Exception as e:
            return jsonResponse(None, 500, "something wrong")
    elif request.method == 'DELETE':
        data = request.get_json()
        try:
            database.deleteSC(data)
            return jsonResponse(None, 200, "success")
        except Exception as e:
            return jsonResponse(None, 500, "something wrong")


@api.route('/Students/count')
def getStudentCount():
    return jsonResponse(database.getStudentCount(), 200, "success")


@api.route('/Courses/count')
def getCourseCount():
    return jsonResponse(database.getCourseCount(), 200, "success")


@api.route('/SCs/count')
def getSCCount():
    return jsonResponse(database.getSCCount(), 200, "success")


server.register_blueprint(api)

if __name__ == '__main__':
    server.run(port=9999, debug=True)
