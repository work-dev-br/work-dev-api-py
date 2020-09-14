from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def root():
    try:
        data = open('index.html').read()    
        return data
    except:
        return geraResponse(400, "Não foi possível abrir o arquivo index.html.")

@app.route("/groups")
def groups():
    groupsList = { "groups": [
        { 
            "id": 1,
            "name": "tips",
            "title": "Dicas",
            "tools": [1, 2, 3]
        },
        { 
            "id": 2,
            "name": "tools",
            "title": "Ferramentas",
            "tools": [1, 2, 4]
        },
        { 
            "id": 3,
            "name": "projects",
            "title": "Projetos",
            "tools": [1, 3, 4]
        },
        { 
            "id": 4,
            "name": "varieties",
            "title": "Variedades",
            "tools": []
        },
    ] }
    return geraResponse( 200, "Consulta concluída com sucesso.", groupsList ) 

@app.route("/tools")
def tools():
    toolsList = { "tools": [
        { 
            "id": 1,
            "name": "reactjs",
            "title": "React JS"
        },
        { 
            "id": 2,
            "name": "nodejs",
            "title": "Node JS"
        },
        { 
            "id": 3,
            "name": "python",
            "title": "Python"
        },
    ] }
    return geraResponse( 200, "Consulta concluída com sucesso.", toolsList ) 

def geraResponse(status, message, content=False):
    response = {}
    response["status"] = status
    response["message"] = message
    if (content):
        response["content"] = content
    return response
