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

TennisMyLife'i avalikud kasutustingimused lubavad isiklikku, õppe- ja mitteärilist uurimiskasutust, kuid ei luba CSV-toorfailide edasijagamist. Seetõttu laadib skript andmed otse algallikast kasutaja arvuti `data/raw/` kausta. See kaust on `.gitignore` failis ja algandmeid repositooriumis ei avaldata.
