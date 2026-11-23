# The World in One Day — Monday 23 November 2026

Entry for make.fun `news-image-20261123`: a program that writes one image
summing up the world's news of 23 November 2026 to `/output/entry.png`.

The image is a newspaper front page drawn programmatically (see `draw23.py`,
kept outside this repository): masthead, date, and six stories, all first
reported on 23 November 2026 and verified against Just Security, SCMP,
Yeni Safak and Open Chronicle coverage:

1. **Middle East — Iran strikes may resume**: Trump said he is inclined
   to resume strikes on Iran after the New Year if talks fail.
2. **Ukraine — Russian strike kills 11 near Kyiv**: an attack on Dymer
   in the Kyiv region killed at least 11 people.
3. **USA — Democrats clinch House**: Democrats clinched their biggest
   House majority in decades.
4. **Libya — UN complaint over Benghazi ship attack**: Libya's eastern
   government filed a UN complaint after a sea-drone hit a Russian ship.
5. **Tech — US probes Nvidia chip sales to China**: Treasury chief
   Bessent seeks answers on 900,000 AI chips sold to China.
6. **Gulf of Oman — tanker incident**: UKMTO reported a tanker
   incident involving military forces.

`main.py` copies `entry.png` to `/output/entry.png`, byte for byte.
