from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory task list (replace with a database for a real app)
tasks = []
@app.route("/")
def index():
    return render_template("index.html", tasks=tasks, zip=zip)
@app.route("/add", methods=["POST"])
def add_task():
    task = request.form["task"]
    tasks.append(task)
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    tasks.pop(task_id)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)