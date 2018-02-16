                    var mymap = L.map('mapid').setView([42.3832, -72.5199], 15);
                    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiZXJtb29yZSIsImEiOiJjamRtZml3c3AwbGJ5MzNvMmpuMGYzaGZ2In0.DZxXS75gos2Oug3nGq1Wzg', {
                    maxZoom: 18,
                    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, ' +
                      '<a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
                      'Imagery © <a href="http://mapbox.com">Mapbox</a>',
                    id: 'mapbox.streets'
                  }).addTo(mymap);

            var marker1 = L.marker([42.4, -72.5199]).addTo(mymap);
            var marker2 = L.marker([42.4, -72.51]).addTo(mymap);
            var marker3 = L.marker([42.35, -72.525]).addTo(mymap);

            marker1.bindPopup("<b>Username</b><br>Currently Listening").openPopup();
            marker2.bindPopup("<b>Username</b><br>Currently Listening").openPopup();
            marker3.bindPopup("<b>Username</b><br>Currently Listening").openPopup();

            var marker4 = L.marker([42.41, -72.6]).addTo(mymap);
            var marker5 = L.marker([42.39, -72.58]).addTo(mymap);
            var marker6 = L.marker([42.43, -72.55]).addTo(mymap);

            marker1.bindPopup("<b>Event Title</b><br>Date<br>Link to more info").openPopup();
            marker2.bindPopup("<b>Event Title</b><br>Date<br>Link to more info").openPopup();
            marker3.bindPopup("<b>Event Title</b><br>Date<br>Link to more info").openPopup();

