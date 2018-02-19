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

            marker1.bindPopup("<b>guitardude53</b><br>Listening to: Fire by Jimi Hendrix<br>Link to profile page").openPopup();
            marker2.bindPopup("<b>TimRichards</b><br>Listening to: Africa by Toto<br>Link to profile page").openPopup();
            marker3.bindPopup("<b>JonesC</b><br>Listening to: Shape of You by Ed Sheeran<br>Link to profile page").openPopup();

            var marker4 = L.marker([42.41, -72.6]).addTo(mymap);
            var marker5 = L.marker([42.39, -72.58]).addTo(mymap);
            var marker6 = L.marker([42.43, -72.55]).addTo(mymap);

            marker4.bindPopup("<b>House Party</b><br>2/19/18<br>Link to event page").openPopup();
            marker5.bindPopup("<b>Jazz Concert</b><br>2/25/18<br>Link to event page").openPopup();
            marker6.bindPopup("<b>Open Mic Night</b><br>2/15/18<br>Link to event page").openPopup();

