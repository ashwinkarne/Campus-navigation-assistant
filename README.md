# 🏫 Campus Navigation Assistant

A simple campus navigation system that helps students find the shortest route between two places inside a college campus.

Instead of figuring out which blocks to go through, the user simply enters their **current location** and **destination**. The system calculates the shortest possible route and displays the result.

---

##  What is this project?

Imagine you're new to a college and don't know where the **Library**, **Computer Lab**, **Canteen**, or **Hostel** is.

This project is built to make campus navigation easier.

The user selects:

**📍 Current Location → 🎯 Destination**

The backend processes the request and uses a shortest-path algorithm to find the route between those locations.

---

## Features

* Select current location
* Select destination
* Find the shortest route
* Calculate route distance
* Fast API-based backend
* Dijkstra's shortest path algorithm
* Campus locations represented using a graph
* Responsive frontend
* Easy to add new locations
* Separate frontend and backend

---

##  How Does It Work?

The campus is represented as a **graph**.

Each important place is a **node**, and the paths between places are represented as **edges** with distances.

For example:

```text
                    Library
                   /       \
                 5          4
                /           \
          Main Gate ---- Fee Payment
              |
              3
              |
           Canteen
```

When the user selects a starting point and destination, the backend checks the available paths and calculates the shortest route.

### Algorithm Used

The project uses **Dijkstra's Shortest Path Algorithm**.

It is useful because different routes can have different distances.

For example:

```text
Main Gate → Library = 5
Main Gate → Canteen = 3
Canteen → Library = 4
```

The algorithm checks the possible paths and finds the route with the minimum total distance.

---

## 🏗️ Project Structure

```text
Campus-navigation-assistant/
│
├── backend/
│   ├── main.py
│   ├── routes.py
│   └── ...
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
│
└── README.md
```

---

##  Tech Stack

### Frontend

* React
* JavaScript
* HTML
* CSS

The frontend provides the interface where users select their locations and view the navigation result.

### Backend

* Python
* FastAPI

FastAPI handles requests from the frontend and performs the route calculation.

### Algorithm

* **Dijkstra's Shortest Path Algorithm**
* Graph data structure

---

##  Application Flow

```text
User
  ↓
Selects Current Location
  ↓
Selects Destination
  ↓
Frontend sends request
  ↓
FastAPI Backend
  ↓
Dijkstra's Algorithm
  ↓
Shortest Route + Distance
  ↓
Frontend displays result
```

---

## 📡 API

The frontend sends the selected locations to the backend using a POST request.

Example request:

```json
{
    "start": "Main Gate",
    "end": "Computer Lab"
}
```

The backend calculates the shortest route and returns the result.

Example:

```json
{
    "route": [
        "Main Gate",
        "Fee Payment Block",
        "Administrative Block",
        "Computer Lab"
    ],
    "distance": 8
}
```

---

## 🏫 Current Campus Locations

The navigation graph currently includes places such as:

* Main Gate
* Fee Payment Block
* Administrative Block
* Library
* Canteen
* CSE Block
* Computer Lab
* Boys Hostel
* Girls Hostel

More locations can be added as the campus graph grows.

---

# 🔮 Future Improvements

The current project is a basic version of the navigation system. There are many things that can be added in future versions.

### 🗺️ 1. Accurate Interactive Campus Map

Instead of displaying only the route information, the application can show an **accurate interactive map of the campus**.

The calculated route can be drawn directly on the map so users can easily understand where they need to go.

---

### 📍 2. Real-Time Location

GPS can be integrated to automatically detect the user's current location.

Instead of manually selecting:

```text
Current Location → Main Gate
```

the application could automatically determine:

```text
📍 You are here
```

and calculate the route from there.

---

### 🧭 3. Live Navigation

The project can eventually provide step-by-step navigation.

For example:

```text
 Walk straight for 100m

 Turn left near the Library

Continue towards CSE Block

🎯 You have reached your destination
```

---

### 🔐 4. User Authentication

Authentication can be added so users can create accounts and securely access the application.

Future authentication features could include:

* User registration
* Login
* Logout
* Password protection
* User profiles
* Secure authentication

This can also allow the application to provide personalized features for different users.

---

### 🚶 5. Walking Distance & Estimated Time

The application can show both distance and approximate walking time.

Example:

```text
Distance: 850 meters
Estimated time: ~11 minutes
```

---

### ♿ 6. Accessible Routes

The system could provide routes suitable for users who require:

* Ramps
* Elevators
* Accessible entrances
* Wheelchair-friendly paths

---

### 🛣️ 7. Multiple Route Options

Instead of showing only one route, the system could provide different options such as:

```text
Shortest Route
Fastest Route
Accessible Route
```

The user can then choose the route based on their needs.

---

### 🏢 8. More Campus Locations

The system can be expanded to include:

* Departments
* Classrooms
* Labs
* Hostels
* Parking areas
* Sports grounds
* Auditoriums
* Cafeterias
* Medical facilities

---

### 👨‍💼 9. Admin Features

An admin system can be introduced in a future version to manage the campus navigation data.

Possible features:

* Add new locations
* Update locations
* Modify routes
* Update distances
* Add or remove campus paths

This would make maintaining the campus map easier without changing the source code manually.

---

### 📱 10. Better Mobile Experience

Future versions can focus more on mobile navigation with:

* Full-screen map
* GPS support
* Touch-friendly controls
* Dark mode
* Location tracking
* Offline campus map

---

## 🎯 Project Goal

The main goal of this project is to make **campus navigation simple, fast and easy to understand**, especially for students who are new to the campus and visitors.

The current version focuses on finding the shortest route using a graph and Dijkstra's algorithm.

In the future, it can grow into a complete **smart campus navigation system** with maps, GPS, authentication and live navigation.

---

## 🚀 Future Vision

```text
Basic Graph
     ↓
Shortest Path
     ↓
Interactive Campus Map
     ↓
GPS Location
     ↓
User Authentication
     ↓
Live Navigation
     ↓
Smart Campus Navigation 🚀
```

---

## 👨‍💻 Built With

**React + FastAPI + Python + Dijkstra's Algorithm**

A college project that turns a basic graph algorithm into a practical campus navigation application.
