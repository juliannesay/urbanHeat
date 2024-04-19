require([
    "esri/Map",
    "esri/views/MapView"
  ], function(Map, MapView) {
  
    var map = new Map({
      basemap: "streets" // Use the Basemap you prefer here
    });
  
    var view = new MapView({
      container: "viewDiv", // Reference to the container's ID
      map: map,
      zoom: 4, // Sets zoom level based on scale
      center: [15, 65] // Sets center point of view using longitude,latitude
    });
    
    // Add any other map functionality you might need here
  
  });
  