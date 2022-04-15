#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from pokemon import Pokemon
import requests
app = Flask(__name__)


@app.route("/start")
@app.route("/")
def start():
    return render_template("pokeindex.html")

@app.route("/search", methods = ['POST', 'GET'])
def search():
    pokemon = Pokemon(request.form.get("pokename").strip().lower(), "","")
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon.pokename}").json()
        pic = response['sprites']['front_default']
        pokemon.pokepic = pic
        p_id = response['id']
        pokemon.pokeid= p_id
    except:
        return render_template("404.html")
    return render_template("pokeindex.html", pokename=pokemon.pokename.title(), pokepic=pokemon.pokepic, pokeid=pokemon.pokeid)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
