import { useState } from "react";
import "./ui_styles.css";

const locations = [
  "Main Gate",
  "Fee Payment Block",
  "Administrative Block",
  "Library",
  "Canteen",
  "Computer Lab",
  "Boys Hostel",
  "Girls Hostel",
];

function CampusNavigator() {
  const [start, setStart] = useState("");
  const [end, setEnd] = useState("");
  const [route, setRoute] = useState([]);
  const [totalDistance, setTotalDistance] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const findRoute = async () => {
    // Validate locations
    if (!start || !end) {
      setError("Please select both locations.");
      return;
    }

    if (start === end) {
      setError("Starting and destination locations cannot be the same.");
      return;
    }

    setError("");
    setLoading(true);
    setRoute([]);
    setTotalDistance(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/route", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          start: start,
          end: end,
        }),
      });

      if (!response.ok) {
        throw new Error(`Server error: ${response.status}`);
      }

      const data = await response.json();

      // Check API response in browser console
      console.log("API Response:", data);

      // Set route
      setRoute(data.path || []);

      /*
        Supports either of these backend responses:

        {
          "path": ["Main Gate", "Canteen", "Library"],
          "total_distance": 8
        }

        OR

        {
          "path": ["Main Gate", "Canteen", "Library"],
          "distance": 8
        }
      */

      const distance = data.total_distance ?? data.distance ?? 0;

      setTotalDistance(distance);

    } catch (err) {
      console.error("Route error:", err);

      setError(
        "Could not connect to the server. Please make sure the FastAPI server is running."
      );

      setRoute([]);
      setTotalDistance(null);

    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="navigator-container">

      {/* Header */}
      <div className="navigator-header">
        <div>
          <p className="small-title">CAMPUS NAVIGATOR</p>

          <h1>Find Your Route</h1>

          <p className="subtitle">
            Select your starting point and destination to find the shortest
            path across campus.
          </p>
        </div>
      </div>


      {/* Search Card */}
      <div className="search-card">

        {/* Current Location */}
        <div className="location-field">
          <label>Current Location</label>

          <select
            value={start}
            onChange={(e) => setStart(e.target.value)}
          >
            <option value="">
              Select current location
            </option>

            {locations.map((location) => (
              <option key={location} value={location}>
                {location}
              </option>
            ))}
          </select>
        </div>


        {/* Direction Icon */}
        <div className="direction-icon">
          ↓
        </div>


        {/* Destination */}
        <div className="location-field">
          <label>Destination</label>

          <select
            value={end}
            onChange={(e) => setEnd(e.target.value)}
          >
            <option value="">
              Select destination
            </option>

            {locations.map((location) => (
              <option key={location} value={location}>
                {location}
              </option>
            ))}
          </select>
        </div>


        {/* Find Route Button */}
        <button
          className="route-button"
          onClick={findRoute}
          disabled={loading}
        >
          {loading
            ? "Finding Route..."
            : "Find Shortest Route"}
        </button>


        {/* Error */}
        {error && (
          <p className="error-message">
            {error}
          </p>
        )}

      </div>


      {/* Route Result */}
      {route.length > 0 && (
        <div className="route-section">

          {/* Route Header */}
          <div className="route-header">

            <div>
              <p className="small-title">
                YOUR ROUTE
              </p>

              <h2>
                Shortest Path
              </h2>
            </div>


            {/* Distance */}
            <div className="distance-box">
              <span>
                Total Distance
              </span>

              <strong>
                {totalDistance ?? 0} m
              </strong>
            </div>

          </div>


          {/* Vertical Route Map */}
          <div className="route-map">

            {route.map((location, index) => (

              <div
                className="route-item"
                key={`${location}-${index}`}
              >

                {/* Marker */}
                <div className="route-marker">
                  {index === 0
                    ? "S"
                    : index === route.length - 1
                    ? "D"
                    : index}
                </div>


                {/* Location Content */}
                <div className="route-content">

                  <h3>
                    {location}
                  </h3>


                  {/* Starting Point */}
                  {index === 0 && (
                    <span className="route-label start-label">
                      Starting Point
                    </span>
                  )}


                  {/* Destination */}
                  {index === route.length - 1 && (
                    <span className="route-label destination-label">
                      Destination
                    </span>
                  )}

                </div>


                {/* Route Line */}
                {index < route.length - 1 && (
                  <div className="route-line">
                    <span>↓</span>
                  </div>
                )}

              </div>

            ))}

          </div>

        </div>
      )}

    </div>
  );
}

export default CampusNavigator;
