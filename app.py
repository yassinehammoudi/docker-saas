from flask import Flask, render_template, request, redirect, url_for
import docker
import os

app = Flask(__name__)
client = docker.from_env()

NGINX_IMAGE = "nginx:latest"
CUSTOM_HTML_PATH = os.path.abspath("nginx")

@app.route("/")
def index():
    containers = client.containers.list(all=True)
    return render_template("index.html", containers=containers)

@app.route("/create", methods=["POST"])
def create_container():
    name = request.form["name"]

    client.containers.run(
        NGINX_IMAGE,
        name=name,
        ports={"80/tcp": None},
        volumes={
            CUSTOM_HTML_PATH: {
                "bind": "/usr/share/nginx/html",
                "mode": "ro"
            }
        },
        detach=True
    )
    return redirect(url_for("index"))

@app.route("/start/<id>")
def start_container(id):
    container = client.containers.get(id)
    container.start()
    return redirect(url_for("index"))

@app.route("/stop/<id>")
def stop_container(id):
    container = client.containers.get(id)
    container.stop()
    return redirect(url_for("index"))

@app.route("/delete/<id>")
def delete_container(id):
    container = client.containers.get(id)
    container.remove(force=True)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
