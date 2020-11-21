from flask import Flask

app = Flask(__name__)

stack = []

@app.route('/stack/push/<data>/')
def push(data): 
    stack.append(data)
    return {"status": "success"}

@app.route('/stack/all')
def all(): 
    return {"elements": stack}

@app.route('/stack/pop/')
def pop():
    popped_element = stack.pop()
    return {"data": popped_element}

@app.route('/stack/TOS/')
def tos():
    tos_element = stack[-1]
    return {"TOS": tos_element}

@app.route('/stack/size/')
def size():
    return {"size": len(stack)}

if __name__ == "__main__":
    app.run()