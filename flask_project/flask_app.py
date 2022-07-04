import requests

from flask import Flask, render_template, request, Response

from Timer import Timer

app = Flask(__name__)

logs_file = "logs.txt"


@app.route("/astro/list")
def get_astro_list():
    with Timer(logs_file, request):
        astros_json = requests.get("http://api.open-notify.org/astros.json").json()
        return render_template("astro.html", astros=astros_json["people"])


@app.route("/astro/craft/<craft_name>")
def get_astro_list_by_craft(craft_name):
    with Timer(logs_file, request):
        astros_json = requests.get("http://api.open-notify.org/astros.json").json()
        return render_template(
            "astro.html", astros=filter(lambda astro: astro["craft"] == craft_name, astros_json["people"]),
        )


@app.route("/file/<file_name>")
def get_file_content(file_name):
    with Timer(logs_file, request):
        file_content: str
        try:
            with open(file_name, "r") as file:
                file_content = file.read()
        except FileNotFoundError:
            return Response(f"Error, there is no {file_name}.")

        return render_template("logfile.html", file_name=file_name, file_content=file_content)


@app.route("/logs")
def get_logs():
    logs: str
    with open(logs_file, "r+") as f:
        logs = f.read()

    return render_template("logfile.html", file_name=logs_file, file_content=logs)


if __name__ == "__main__":
    app.run(debug=True)
