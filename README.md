# Geo Processor - FastAPI Backend

## How to run
First of all you need to ensure using python 3.13, a virtual environment and install all dependencies:

```sh
pip install -r requirements.txt
```

To run FastAPI application at [localhost](http://localhost:8000) (or [docs](http://localhost:8000/docs)) you can run

```sh
# development
fastapi dev main.py
# production
gunicorn main:app
```

## Endpoints

### POST /coords/process

Given a list of coordinates it calculates and returns centroid and bounds (north, south, east, west).

**Body**

Dictionary containing a list of `points`, each point has a `lat` and `lng`.

```json
{
  "points": [{ "lat": 0.0, "lng": 0.0 }]
}
```

**Responses**

- **200: OK** Returns dictionary containing calculated `centroid` coordinates and `bounds` limits.

```json
{
  "centroid": { "lat": 0.0, "lng": 0.0 },
  "bounds": {
    "north": 0.0,
    "south": 0.0,
    "east": 0.0,
    "west": 0.0
  }
}
```

- **400: Bad request**. Returns dictionary with `error` message.

```json
{
  "error": "..."
}
```
