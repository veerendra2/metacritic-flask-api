#!/usr/bin/python3
"""
Metacritic API
"""

import json
import requests
import logging
import os

import flask
from urllib.parse import unquote
from bs4 import BeautifulSoup
from waitress import serve

__author__ = "Veerendra.Kakumanu"


def get_page():
    '''
    Gets html page content

    :return: string   
    '''
    global api_url
    headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) Gecko/20100101 Firefox/98.0'
    }
    res = requests.get(api_url, headers=headers)
    return(res.text)

def parse_html(game_name=None):
    '''
    Parses html page content

    :param game_name: Name of the game to retrive details
    :type game_name: string
    :return: string   
    '''
    games_list = list()
    html_content = get_page()
    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find("table", {"class": "clamp-list"})
    tds = table.find_all("td", {"class": "clamp-summary-wrap"})
    for data in tds:
        cur_game_name = data.find('h3').text.strip()
        temp_dict = {
                "title": cur_game_name,
                "score": data.find('div', {"class": "metascore_w large game positive"}).text.strip()
            }
        if game_name is not None and cur_game_name == game_name:
            return temp_dict
        games_list.append(temp_dict)
    if game_name is None:
        return(games_list)
    else:
        return "{}"


app = flask.Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h2>Available APIs<h2> /games <br> /games/TITLE_OF_GAME"

@app.route('/games/<game_name>', methods=['GET'])
def get_game(game_name):
    return flask.json.jsonify(parse_html(unquote(game_name)))

@app.route('/games/', methods=['GET'])
def get_top_games():
    return flask.json.jsonify(parse_html())

def main():
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
    global api_url
    try: 
        port = os.environ["PORT"]
        api_url = os.environ["URL"]
    except KeyError: 
        logging.error("Please set the environment variable(s) PORT and URL")
        exit(1)
    serve(app, host='0.0.0.0', port=port)


if __name__ == '__main__':
    main()