#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask import jsonify
import requests

app= Flask(__name__)

pokemon= [{
    'name': 'Bulbasaur',
    'id': 1,
    'type': ['grass','poison'],
    'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png'
        },{
    'name': 'Squirtle',
    'id': 7,
    'type': ['water'],
    'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/7.png'
    },{
    'name': 'Charmander',
    'id': 4,
    'type': ['fire'],
    'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/4.png'
    },{
     'name': 'Pikachu',
    'id': 25,
    'type': ['electric'],
    'image': 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png'
       }]


@app.route("/json")
def json():
    return jsonify(pokemon)

@app.route("/")
def index():
    return render_template("index.html", pokemonlist=pokemon )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)