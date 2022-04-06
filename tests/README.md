# Tests
A test case script for metacritic-api application

## Run
```
$ pip3 install requirements.txt
$ python test.py 
INFO:Hitting /games
DEBUG:Starting new HTTP connection (1): localhost:80
DEBUG:http://localhost:80 "GET /games HTTP/1.1" 308 272
DEBUG:http://localhost:80 "GET /games/ HTTP/1.1" 200 463
DEBUG:Status: 200, Elapsed Time: 0.37267, Data: [{'score': '90', 'title': 'Horizon Forbidden West'}, {'score': '86', 'title': 'OlliOlli World'}, {
'score': '83', 'title': 'Infernax'}, {'score': '82', 'title': 'The King of Fighters XV'}, {'score': '81', 'title': 'Persona 4 Arena Ultimax'}, {'s
core': '81', 'title': 'Atelier Sophie 2: The Alchemist of the Mysterious Dream'}, {'score': '79', 'title': 'Vagante'}, {'score': '79', 'title': 'R
ise of the Third Power'}, {'score': '77', 'title': 'Young Souls'}, {'score': '76', 'title': 'Conan Chop Chop'}]
INFO:Hitting /games/{} with data
DEBUG:Starting new HTTP connection (1): localhost:80
DEBUG:http://localhost:80 "GET /games/Horizon%20Forbidden%20West HTTP/1.1" 200 48
DEBUG:Status: 200, Elapsed Time: 0.368569, Data: {'score': '90', 'title': 'Horizon Forbidden West'}
DEBUG:Starting new HTTP connection (1): localhost:80
DEBUG:http://localhost:80 "GET /games/OlliOlli%20World HTTP/1.1" 200 40
DEBUG:Status: 200, Elapsed Time: 0.346937, Data: {'score': '86', 'title': 'OlliOlli World'}
DEBUG:Starting new HTTP connection (1): localhost:80
DEBUG:http://localhost:80 "GET /games/Infernax HTTP/1.1" 200 34
DEBUG:Status: 200, Elapsed Time: 0.338794, Data: {'score': '83', 'title': 'Infernax'}
DEBUG:Starting new HTTP connection (1): localhost:80
DEBUG:http://localhost:80 "GET /games/The%20King%20of%20Fighters%20XV HTTP/1.1" 200 49
DEBUG:Status: 200, Elapsed Time: 0.335549, Data: {'score': '82', 'title': 'The King of Fighters XV'}
DEBUG:Starting new HTTP connection (1): localhost:80
DEBUG:http://localhost:80 "GET /games/Persona%204%20Arena%20Ultimax HTTP/1.1" 200 49
DEBUG:Status: 200, Elapsed Time: 0.346102, Data: {'score': '81', 'title': 'Persona 4 Arena Ultimax'}
DEBUG:Starting new HTTP connection (1): localhost:80
DEBUG:http://localhost:80 "GET /games/Atelier%20Sophie%202:%20The%20Alchemist%20of%20the%20Mysterious%20Dream HTTP/1.1" 200 81
DEBUG:Status: 200, Elapsed Time: 0.351633, Data: {'score': '81', 'title': 'Atelier Sophie 2: The Alchemist of the Mysterious Dream'}
DEBUG:Starting new HTTP connection (1): localhost:80
DEBUG:http://localhost:80 "GET /games/Vagante HTTP/1.1" 200 33
DEBUG:Status: 200, Elapsed Time: 0.341412, Data: {'score': '79', 'title': 'Vagante'}
DEBUG:Starting new HTTP connection (1): localhost:80
DEBUG:http://localhost:80 "GET /games/Rise%20of%20the%20Third%20Power HTTP/1.1" 200 49
DEBUG:Status: 200, Elapsed Time: 0.322231, Data: {'score': '79', 'title': 'Rise of the Third Power'}
DEBUG:Starting new HTTP connection (1): localhost:80
DEBUG:http://localhost:80 "GET /games/Young%20Souls HTTP/1.1" 200 37
DEBUG:Status: 200, Elapsed Time: 0.356636, Data: {'score': '77', 'title': 'Young Souls'}
DEBUG:Starting new HTTP connection (1): localhost:80
DEBUG:http://localhost:80 "GET /games/Conan%20Chop%20Chop HTTP/1.1" 200 41
DEBUG:Status: 200, Elapsed Time: 0.331561, Data: {'score': '76', 'title': 'Conan Chop Chop'}
```