![games(24)](https://github.com/user-attachments/assets/a348827e-890e-4c41-9432-fc3a2d540cfd)

A web-based flight simulator game where your mission is to purify a polluted Earth. Built using **Python(Flask)**, **JavaScript**, **HTML**, **CSS**, and a **PostgreSQL** database.

<p align="center">
<img src="https://github.com/user-attachments/assets/f3629ba6-1905-4a68-a681-f1bc2c64e980" alt="Description" >
</p>

######  To live in a space station, what an honour...
Years ago you were selected among millions to be one of the few lucky individuals to take part in an experiment started by the World Government. As one of the chosen few, you had the opportunity to look down upon Earth in all its glory. Months later, you noticed that the Earth no longer looked as it once did. 
As it turns out, this was the reason behind the whole experiment.

Earth doesn't have much more time. The polluted world you see before you is a product of the unsustainable lifestyle of humans. No one else on the space station shared your worries about the pollution taking over Earth. You knew you had to take action, even if you were alone. With your trusty space-made purification gun and only a few minutes to spare, you hijack an escape pod and make your way to Earth to purify the spreading pollution. Landing right outside an airport, you come across an old airplane with a limited CO₂ amount.

Fly around to all the countries and purify Earth as you go. The fate of Earth is in your hands; however, your fate is in the hands of bored higher beings who like to throw dice. With enough luck, you may be able to succeed.

## Key Game Features
###### Flight System
Fly between real airports across 50 EU countries. Each airport has real coordinates 
and country info pulled from the database.
###### CO₂ Management
Each flight consumes CO₂ based on distance. Exceeding your budget ends the game.
###### Dice of Fate Mechanic
Each flight rolls a 1-6 die:

 1: Game over
 
 2: Detour (Double CO₂)
 
 3: Wrong destination (Random airport)
 
 4: Return to previous airport (Wasted CO₂)
 
 5: 50% CO₂ refund
 
 6: Full CO₂ refund
 
###### Goal Tracking
Collected countries are tracked in the database. Every 10 countries reduces global pollution by 20%.
###### Live Weather Display
Fetches weather for each location (e.g., clear, windy, cloudy) using the OpenWeatherMap API.
###### Country Facts
Fetches country information when visiting each location.
###### Game Timer
You have 3 minutes to purify all 50 countries before Earth is doomed.

<p align="center">
<img src="https://github.com/user-attachments/assets/ab388f3b-8894-4c67-8b7f-824c5c469153" alt="Description" >
</p>




## Technologies Used
Python + Flask – Backend game logic and APIs.

PostgreSQL  – Stores player data, airport info, and game progress.

HTML/CSS/JavaScript  – Frontend and user interactions.

OpenWeatherMap API  – Real-time weather at each airport.

GeoPy  – Calculates distances between airports


