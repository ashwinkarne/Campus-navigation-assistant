from fastapi import APIRouter
from models import RouteRequest

router = APIRouter()


graph = {
    "Main Gate": {
        "Fee Payment Block": 2,
        "Library": 5,
        "Canteen": 3
    },

    "Fee Payment Block": {
        "Main Gate": 2,
        "Administrative Block": 2,
        "Library": 4
    },

    "Administrative Block": {
        "Fee Payment Block": 2,
        "CSE Block": 3,
        "Computer Lab": 4
    },

    "Library": {
        "Main Gate": 5,
        "Fee Payment Block": 4,
        "Canteen": 2,
        "Computer Lab": 3,
        "CSE Block": 4
    },

    "Canteen": {
        "Main Gate": 3,
        "Library": 2,
        "Boys Hostel": 5,
        "Girls Hostel": 6
    },

    "CSE Block": {
        "Administrative Block": 3,
        "Library": 4,
        "Computer Lab": 2,
        "Boys Hostel": 4
    },

    "Computer Lab": {
        "Administrative Block": 4,
        "Library": 3,
        "CSE Block": 2,
        "Girls Hostel": 4
    },

    "Boys Hostel": {
        "Canteen": 5,
        "CSE Block": 4,
        "Girls Hostel": 3
    },

    "Girls Hostel": {
        "Canteen": 6,
        "Computer Lab": 4,
        "Boys Hostel": 3
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

    if request.algorithm == "dijkstra":
        return dijkstra(start, end)

    return {
        "error": "Algorithm not supported"
    }


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
        "algorithm": "dijkstra",
        "start": start,
        "end": end,
        "distance": distances[end],
        "path": path
    }