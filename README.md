# Sähkönhinnan Ennustus

Tämä on osa Ohjelmistokehitystiimin jäsenenä toimiminen -näyttötehtävää. Tehtävän tavoitteena on luoda SmartHome-sovellukseen sivu, joka ennustaa sähkön hintaa 12 tuntia eteenpäin säätietojen perusteella.

## Käyttöönotto

1. Asenna tarvittavat riippuvuudet:

   ```bash
   pip install requests
Aseta OpenWeatherMap API-avain muuttujaan api_avain tiedostossa electricity_prediction.py.

Määritä halutut kaupungit listana muuttujaan kaupungit tiedostossa electricity_prediction.py.

Suorita koodi: python electricity_prediction.py

Saadut tiedot

Ohjelma hakee säätiedot valituista kaupungeista OpenWeatherMapin API:sta ja palauttaa ne sanakirjana, joka sisältää lämpötilan ja tuulen nopeuden kullekin kaupungille.
Tärkeät Huomiot

    Varmista, että OpenWeatherMap API-avain on voimassa ja lisätty oikein.
    Tämä on yksinkertainen esimerkki ja voi vaatia laajempaa kehitystä riippuen projektitavoitteista.
