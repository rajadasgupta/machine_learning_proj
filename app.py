from flask import Flask

app=Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    return "This is my first flask ML project. Also established the CI/CD pipleline"


if __name__ =="__main__":
    app.run(debug=True)
    
