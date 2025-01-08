# coopmaster-room-driver

Aplikace provazuje core aplikace(konkrétně službu room assistant) s arduinem ovladajicim svetla, dvere a poskytujici informaci o teplote a vzdusne vlhkosti.
Součástí projektu je i firmware arduina.

## funkcionalita
- umoznuje ovladat osvetleni kurniku
- resi otevírání a zavírání dvířek v kurníku
- ziskava informace ze senzoru o teplote a vlhkosti v kurniku
- komunikuje se zbytkem systému pomocí rest api
- s arduinem komunikuje pomocí serialového portu a pomocí zasílání příkazů v podobě jednoho písmene
- příkazy: o = otevřít dvířka, c = zavřít dvířka, l = rozsvítit světlo, d = zhasnout světlo, j = vrátí json s daty o teplotě a vlhkosti, s = vrátí json s daty o stavech jednotlivých ovládaných prvku (dvěře, světlo) 

## technologie
- python
- c++ / wire (jazyk pro programování v arduino ide)
- knihovny pro python
  - **Flask**: Lehký webový framework, flexibilní a rychlý vývoj webových aplikací.
  - **colorama**: Manipulace s barvami v textovém výstupu na terminálu.
  - **waitress**: Rychlý WSGI server pro produkční nasazení webových aplikací.
  - **APScheduler**: Plánování a automatizace úloh v Pythonu.
  - **requests**: Jednoduché HTTP požadavky (GET, POST, atd.).
  - **Werkzeug**: WSGI nástroje pro webové aplikace (routování, správa relací).
  - **python-dotenv**: Načítání konfigurace z `.env` souborů.
  - **pyserial**: Komunikace se sériovými zařízeními přes sériové porty.
- knihovny pro arduino
  - defaultní **Arduino.h**
  - **DHT**: pro ovládání teplotních+vlhkostních sezorů DHT11 a DHT22 

## hardware
- arduino Nano v3.0
- teplotni a vlhkosti senzor DHT11
- samotana konstrukce dveri
- relatko ovladajici svetlo a relátka udávající chod a směr motoru
- napájeno připojením ke raspberry pi přes usb napětím 5V

## konstrukce dveri - expoziční
- přímočarý motor s dorazy
- konstrukce z hliníkových profilů a smontnotváno pomocí běžných spojovacích prvků pro práci s těmito profily
- dvířka reprezentována hliníkovým plátem tahaným lankem připěvněným k ramenu který vynáší sílu od motoru k dvířkům
- zdroj 12V
## konstrukce dveri - instalováno
- zdroj 12V
- rám z železných U profilů použitých jako vodící lišty pro posuv dvířek z plastové desky a pásků které konstrukci udžují po kupě
- naviják je s dvířky přopojen lankem
- navijecí systém / systém navijáku
  - 12V motor s převodovkou, rychlostí otáčení 60rpm
  - navíjecí buben vytištěný na 3d tiskárně
  - dorazový systém 
