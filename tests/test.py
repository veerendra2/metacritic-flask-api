#!/usr/bin/python3
'''
Author: Veerendra Kakumanu
Description: Test script for metacritic api
'''
import requests
import logging

SERVER_PORT = 80
URL = "http://localhost"
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

API_LIST = [
    "/games",
    "/games/{}"
]

def fetch(endpoint, url=URL, port=SERVER_PORT):
    res = requests.get(f"{url}:{port}{endpoint}")
    return (res.json(), res.status_code, res.elapsed.total_seconds())

def main():
    logging.info(f"Hitting {API_LIST[0]}")
    data, status, elapsed_time = fetch(endpoint=API_LIST[0])
    logging.debug(f"Status: {status}, Elapsed Time: {elapsed_time}, Data: {data}")
    logging.info(f"Hitting {API_LIST[1]} with data")
    for game in data:
        endpoint = API_LIST[1].format(game['title'])
        data, status, elapsed_time = fetch(endpoint=endpoint)
        logging.debug(f"Status: {status}, Elapsed Time: {elapsed_time}, Data: {data}")


if __name__ == '__main__':
    main()