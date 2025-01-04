# coopmaster-room-driver

Aplikace provazuje core aplikace s arduinem ovladajici svetla, dvere a poskytujici informaci o teplote a vzdusne vlhkosti.

## funkcionalita
- umoznuje ovladat osvetleni kurniku
- resi rano otevirani dveri kurniku a vecer zavirani 
- ziskava informace ze senzoru o teplote a vlhkosti v kurniku
- dvere se nezavrou pokud nejsou slepice doma
- dvere v modu automatickeho zavirani si volaji o data kdy zavirat https://kodim.cz/czechitas/daweb/js2/server-komunikace/cv-volani-api/vychod-zapad 
- Integrace se sluzbou  - https://api.sunrise-sunset.org/json?lat=50&lng=14.5

## technologie
- python
- c++
- knihovny - popis jednotlivych knihoven

## hardware
- arduino Mini
- prevodnik analog/digital
- teplotni a vlhkosti senzor
- samotana konstrukce dveri
- relatka ovladajici svetlo

## konstrukce dveri
- tahlovy motor
- bowden
- doraz
