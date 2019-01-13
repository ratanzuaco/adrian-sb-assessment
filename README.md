# Gender Guess API

This RESTful API allows you to:
- 'poke' the system through a GET request and
- make the system guess your gender (by providing it with your name) through a POST request.

## Project (Assessment) links:
- DockerHub (image repo): [a link](https://cloud.docker.com/u/ratanzuaco/repository/docker/ratanzuaco/adrian-sb-assessment-docker)
- GitHub (code repo): [a link](https://github.com/ratanzuaco/adrian-sb-assessment)
- AWS (platform): [a link]()
- REST endpoint: [a link](http://18.217.255.145)

### Instructions

#### GET method

****REQUEST****
'GET http://18.217.255.145:5315/guessgender'

****RESPONSE****
('...snappy comment...')

#### POST method

****REQUEST****
'POST http://18.217.255.145:5315/guessgender'

'''JSON
{"name":"[name]"}
'''

****RESPONSE****
('...gender guess response...')
