from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tareas = [0]

@app.route("/")
def home():
    return render_template("index.html", tareas=tareas[-1])


@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "GET":
        return render_template("agregar.html")
    else:
        tarea = request.form.get("tarea")
        tareas.append(tarea)
        return redirect("/")


@app.route("/api/tareas", methods=["GET", "POST"])
def api_tareas():
    return {"tareas": tareas[-1]}
