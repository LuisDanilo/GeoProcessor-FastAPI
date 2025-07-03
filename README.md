# Docs

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
