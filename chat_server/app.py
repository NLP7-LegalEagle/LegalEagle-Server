import json
from flask import Flask, request, jsonify
from enum import Enum
from Llama import *


### -- Error Handling -- ###
class ServerError(Enum):
    InvalidInputTextError = ("Invaild Input Text Error", "Input text is invalid")
    ModelError = ("Model Error", "Model is not loaded")

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def message(self):
        return f"Error:{self.title}\n({self.description})"

### -------------------- ###
###       Server         ###
### -------------------- ###

app = Flask(__name__)

model = Llama()

@app.route('/text_generation', methods=['POST'])
def text_generation():
    # MARK: - Error Check
    data = checkError(request.get_json())
    if isinstance(data, ServerError):
        response_dict = {"error": data.title, "error_description": data.description}
        return json.dumps(response_dict)

    # MARK: - Data Handling
    input_text = data["input_text"]
    output = model.text_generation(input_text)

    # MARK: - Response Generation
    response_dict = {"output": output}
    response = json.dumps(response_dict)
    return response


def checkError(data: dict):
    if model is None:
        return ServerError.ModelError
    if "input_text" not in data.keys():
        return ServerError.InvalidInputTextError
    return data


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1525)
