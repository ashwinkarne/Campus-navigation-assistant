from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class RouteRequest(BaseModel):
    start: str
    end: str


graph = {
    "Main Gate": {
        "Fee Payment Block": 120,
        "Library": 180,
        "Canteen": 150
    },

    "Fee Payment Block": {
        "Main Gate": 120,
        "Administrative Block": 100,
        "Library": 160
    },

    "Administrative Block": {
        "Fee Payment Block": 100,
        "CSE Block": 140,
        "Computer Lab": 180
    },

    "Library": {
        "Main Gate": 180,
        "Fee Payment Block": 160,
        "Canteen": 90,
        "Computer Lab": 130,
        "CSE Block": 150
    },

    "Canteen": {
        "Main Gate": 150,
        "Library": 90,
        "Boys Hostel": 220,
        "Girls Hostel": 260
    },

    "CSE Block": {
        "Administrative Block": 140,
        "Library": 150,
        "Computer Lab": 80,
        "Boys Hostel": 180
    },

    "Computer Lab": {
        "Administrative Block": 180,
        "Library": 130,
        "CSE Block": 80,
        "Girls Hostel": 170
    },

    "Boys Hostel": {
        "Canteen": 220,
        "CSE Block": 180,
        "Girls Hostel": 120
    },

    "Girls Hostel": {
        "Canteen": 260,
        "Computer Lab": 170,
        "Boys Hostel": 120
    }
}


@router.post("/route")
def find_route(request: RouteRequest):

    start = request.start
    end = request.end

    if start not in graph or end not in graph:
        return {
            "error": "Invalid location"
        }

    return dijkstra(start, end)


def dijkstra(start, end):

    distances = {
        location: float("inf")
        for location in graph
    }

    previous = {
        location: None
        for location in graph
    }

    distances[start] = 0

    unvisited = list(graph.keys())

    while unvisited:

        current = min(
            unvisited,
            key=lambda location: distances[location]
        )

        unvisited.remove(current)

        if current == end:
            break

        for neighbor, distance in graph[current].items():

            new_distance = distances[current] + distance

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current

    path = []
    current = end

    while current is not None:
        path.append(current)
        current = previous[current]

    path.reverse()

    return {
        "start": start,
        "end": end,
        "distance": distances[end],
        "path": path
    }