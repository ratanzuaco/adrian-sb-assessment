# Gender Guess API

This RESTful API allows you to:
- 'poke' the system through a GET request and
- make the system guess your gender (by providing it with your name) through a POST request.

## Project (Assessment) links:
- DockerHub (image repo): [https://cloud.docker.com/u/ratanzuaco/repository/docker/ratanzuaco/adrian-sb-assessment-docker](https://cloud.docker.com/u/ratanzuaco/repository/docker/ratanzuaco/adrian-sb-assessment-docker)
- GitHub (code repo): [https://github.com/ratanzuaco/adrian-sb-assessment](https://github.com/ratanzuaco/adrian-sb-assessment)
- AWS (platform): []()
- REST endpoint: [http://18.217.255.145:5315](http://18.217.255.145:5315)

### Instructions

#### GET method

****REQUEST****
`GET http://18.217.255.145:5315/guessgender`

****RESPONSE****
`('...snappy comment...')`

#### POST method

****REQUEST****
`POST http://18.217.255.145:5315/guessgender`

```JSON
{"name":"[name]"}
```

****RESPONSE****
`('...gender guess response...')`
