from pydantic import BaseModel

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()


class Point(BaseModel):
    """Model that represents a coordinate with latitude and longitude"""

    lat: float
    lng: float


class CoordsReqBody(BaseModel):
    """Request body for processing coordinates"""

    points: list[Point]


@app.get("/")
def root():
    """Root endpoint"""
    return {"data": "Hello world"}, 200


@app.post("/coords/process")
def process_coordinates(coords: CoordsReqBody):
    """
    Endpoint for processing a list of coordinates and calcualting the centroid and bounds

    Args:
        coords (CoordsReqBody): An object containing a list of points, where each point has 'lat' and 'lng' attributes.

    Returns:
        dict: A dictionary with the calculated centroid and bounds (north, south, east, west limits).

    Raises:
        Returns an error message and status code 400 if the input is invalid or an exception occurs during processing.
    """

    # Get points from body request
    points = coords.points

    # Validate point list
    if not points or not isinstance(points, list):
        return JSONResponse(
            content={"error": "Point list was not provided."},
            status_code=400,
        )

    # Init variables for centroid and bounds
    c_lat = 0
    c_lng = 0
    north = points[0].lat
    south = points[0].lat
    east = points[0].lng
    west = points[0].lng

    try:
        # Calculate centroid and bounds
        for point in points:
            c_lat += point.lat
            c_lng += point.lng
            north = max(north, point.lat)
            south = min(south, point.lat)
            east = max(east, point.lng)
            west = min(west, point.lng)

        # Format results
        centroid = {
            "lat": round(c_lat / len(points), 4),
            "lng": round(c_lng / len(points), 4),
        }
        bounds = {
            "north": round(north, 4),
            "south": round(south, 4),
            "east": round(east, 4),
            "west": round(west, 4),
        }

        # Return results
        return JSONResponse(
            content={"centroid": centroid, "bounds": bounds},
            status_code=200,
        )
    except Exception as e:
        # Handle any exception during processing
        return JSONResponse(
            content={
                "error": f"An error occurred while processing the points: {str(e)}"
            },
            status_code=400,
        )
