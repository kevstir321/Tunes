(function() {

  var basemaps = {
    Grayscale: L.tileLayer('http://{s}.tiles.wmflabs.org/bw-mapnik/{z}/{x}/{y}.png', {
      maxZoom: 18,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    }),
    Streets: L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
      attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
    })
  };

  var groups = {
    people: new L.LayerGroup(),
    events: new L.LayerGroup()
  };

  L.marker([42.3832, -72.5199]).bindPopup("<b>Username</b><br>Currently Listening").addTo(groups.people);
  L.marker([42.4832, -72.5199]).bindPopup("<b>Username</b><br>Currently Listening").addTo(groups.people);
  L.marker([42.5832, -72.5199]).bindPopup("<b>Username</b><br>Currently Listening").addTo(groups.people);
  L.marker([42.6832, -72.5199]).bindPopup("<b>Username</b><br>Currently Listening").addTo(groups.people);

  L.marker([42.3832, -72.4199]).bindPopup("<b>Event Title</b><br>Date<br>Link to more info").addTo(groups.events);
  L.marker([42.3832, -72.3199]).bindPopup("<b>Event Title</b><br>Date<br>Link to more info").addTo(groups.events);
  L.marker([42.3832, -72.2199]).bindPopup("<b>Event Title</b><br>Date<br>Link to more info").addTo(groups.events);
  L.marker([42.3832, -72.1199]).bindPopup("<b>Event Title</b><br>Date<br>Link to more info").addTo(groups.events);

  window.ExampleData = {
    LayerGroups: groups,
    Basemaps: basemaps
  };

}());