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

  L.marker([42.3832, -72.5199]).bindPopup("<b>guitardude53</b><br>Listening to: Fire by Jimi Hendrix<br>Link to profile page").addTo(groups.people);
  L.marker([42.4832, -72.5199]).bindPopup("<b>TimRichards</b><br>Listening to: Africa by Toto<br>Link to profile page").addTo(groups.people);
  L.marker([42.5832, -72.5199]).bindPopup("<b>JonesC</b><br>Listening to: Shape of You by Ed Sheeran<br>Link to profile page").addTo(groups.people);
  L.marker([42.6832, -72.5199]).bindPopup("<b>evanm31</b><br>Listening to: In the Air III by Tim Hecker<br>Link to profile page").addTo(groups.people);

  L.marker([42.3832, -72.4199]).bindPopup("<b>House Party</b><br>2/19/18<br>Link to event page").addTo(groups.events);
  L.marker([42.3832, -72.3199]).bindPopup("<b>Jazz Concert</b><br>2/25/18<br>Link to event page").addTo(groups.events);
  L.marker([42.3832, -72.2199]).bindPopup("<b>Open Mic Night</b><br>2/15/18<br>Link to event page").addTo(groups.events);
  L.marker([42.3832, -72.1199]).bindPopup("<b>Jam Session</b><br>2/30/18<br>Link to event page").addTo(groups.events);

  window.ExampleData = {
    LayerGroups: groups,
    Basemaps: basemaps
  };

}());