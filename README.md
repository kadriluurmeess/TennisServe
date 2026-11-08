# TennisServe

**Project E7: Serve Performance and Match Outcomes in Tennis: A Focus on Kanepi and Kontaveit**

Meeskond: Kadri Luurmees ja Triin Aabreldaal.

Projekt uurib esimese servi õnnestumisprotsendi ning esimeselt ja teiselt servilt võidetud punktide seost mängu võitmisega. Lisaks võrdleme Kaia Kanepi ja Anett Kontaveidi servinäitajaid ning võiduprotsente sarnase edetabelikohaga mängijatega, arvestades väljakukatet ja vastaste tugevust.

## Andmed

Allikas: [TennisMyLife – Tennis Match Database](https://stats.tennismylife.org/tennis-match-database).

Kasutame kuut WTA üksikmängude aastafaili: `2018_wta.csv` kuni `2023_wta.csv`. Üks algandmestiku rida kirjeldab ühte mängu ning sisaldab nii võitja kui ka kaotaja andmeid.

2026-11-08 algallikast alla laaditud failides kontrollitud maht: **14 776 rida ja 50 veergu** enne puhastamist. Kõigil kuuel failil on samad veerud samas järjekorras.

| Aasta | Ridade arv | Veergude arv |
| --- | ---: | ---: |
| 2018 | 2756 | 50 |
| 2019 | 2743 | 50 |
| 2020 | 1276 | 50 |
| 2021 | 2597 | 50 |
| 2022 | 2594 | 50 |
| 2023 | 2810 | 50 |
| Kokku | 14776 | 50 |

TennisMyLife'i avalikud kasutustingimused lubavad isiklikku, õppe- ja mitteärilist uurimiskasutust, kuid ei luba CSV-toorfailide edasijagamist. Seetõttu laadib skript andmed otse algallikast kasutaja arvuti `data/raw/` kausta. See kaust on `.gitignore` failis ja algandmeid repositooriumis ei avaldata. Enne muud kasutust kontrollige allika kehtivaid tingimusi.

## Käivitamine

1. Laadige repositoorium oma arvutisse ja avage selle kaust terminalis.
2. Laadige andmed alla (vajalik Python 3; skript kasutab ainult standardteeki):

   ```bash
   python download_data.py
   ```

   Windowsis võib kasutada ka `py download_data.py`. Skript prindib iga aasta ridade ja veergude arvu ning koguarvu. Olemasolevaid faile ei laadita uuesti ega kirjutata üle. Algallikas võib hiljem andmeid parandada; kordusanalüüsiks säilitage kohalikud failid.

3. Märkmiku jaoks paigaldage vajalikud paketid:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Avage `andmete_ulevaade.ipynb` Jupyteris või VS Code'is ja käivitage lahtrid järjekorras. Märkmik kasutab sama allalaadimisskripti, ühendab aastafailid ning näitab ridade ja veergude arvu.

Veebis kuvatava märkmiku väljundid on jäetud tühjaks, et toorandmete ridu mitte edasi jagada. Need tekivad märkmiku käivitamisel kohalikus arvutis.
