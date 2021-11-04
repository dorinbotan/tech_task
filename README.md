# Structure

The solution consists of 4 components:

1. Web frontend, written in `React` and served as a static website over `Nginx`

2. REST API, written in `Python`/`FastAPI` and served over `Uvicorn`

3. `MongoDB` filled with the provided data

4. `Nginx` API gateway, forwarding all incoming requests to the Web frontend or the API based on the URL 

There are 3 publicly accessible endpoints, all running on port 80:

1. `/` - Web frontend

2. `/api/*` - API

3. `/docs` - Swagger UI

# Deployment

The system is defined as a single Docker compose configuration. Therefore, it can be started by executing the following command in the rood folder:

    docker-compose up

# Things to consider

- Storing 1000 records in an on-disk database, as well as splitting the system into 4 components is excessive. The intension was to show what a production-grade system would look like.

- Complete lack of tests, pushing to master branch and lack of documentation are only justified by the limited amount of time available and the fact that the system is not intended for real-world use.
