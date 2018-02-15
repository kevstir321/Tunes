(function() {

  var groups = {
    people: new L.LayerGroup(),
    events: new L.LayerGroup()
  };

  L.marker([42.3832, -72.5199]).bindPopup('Littleton, CO.').addTo(groups.people);
  L.marker([42.4832, -72.5199]).bindPopup('Denver, CO.').addTo(groups.people);
  L.marker([42.5832, -72.5199]).bindPopup('Aurora, CO.').addTo(groups.people);
  L.marker([42.6832, -72.5199]).bindPopup('Golden, CO.').addTo(groups.people);

  L.marker([42.3832, -72.4199]).bindPopup('A restaurant').addTo(groups.events);
  L.marker([42.3832, -72.3199]).bindPopup('A restaurant').addTo(groups.events);
  L.marker([42.3832, -72.2199]).bindPopup('A restaurant').addTo(groups.events);
  L.marker([42.3832, -72.1199]).bindPopup('A restaurant').addTo(groups.events);

  window.ExampleData = {
    LayerGroups: groups,
  };

}());