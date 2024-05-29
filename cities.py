class City():
    def __init__(self) -> None:
        self.cities = {
            'London': 'https://www.metoffice.gov.uk/weather/forecast/gcpvj0v07#?date=2024-05-29',
            'Bath': 'https://www.metoffice.gov.uk/weather/forecast/gcnk62de6#?date=2024-05-29',
            'Bradford': 'https://www.metoffice.gov.uk/weather/forecast/gcwdpcpzj',
            'Brighton and Hove': 'https://www.metoffice.gov.uk/weather/forecast/gcpcq5541',
            'Birmingham': 'https://www.metoffice.gov.uk/weather/forecast/gcqdt4b2x',
            'Bristol': 'https://www.metoffice.gov.uk/weather/forecast/gcnhtnumz',
            'Cambridge': 'https://www.metoffice.gov.uk/weather/forecast/u1214b469',
            'Canterbury': 'https://www.metoffice.gov.uk/weather/forecast/u10g8x4vg',
            'Carlisle': 'https://www.metoffice.gov.uk/weather/forecast/gcvbs84rv#?date=2024-05-29',
            'Chelmsford': 'https://www.metoffice.gov.uk/weather/forecast/u10q6cgzm#?date=2024-05-29',
            'Chester': 'https://www.metoffice.gov.uk/weather/forecast/gcmyw5w26#?date=2024-05-29',
            'Chichester': 'https://www.metoffice.gov.uk/weather/forecast/gcp3nqsgd#?date=2024-05-29',
            'Coventry': 'https://www.metoffice.gov.uk/weather/forecast/gcqfjkq3z#?date=2024-05-29',
            'Derby': 'https://www.metoffice.gov.uk/weather/forecast/gcqvn6pq4#?date=2024-05-29',
            'Doncaster': 'https://www.metoffice.gov.uk/weather/forecast/gcx0qr7rt#?date=2024-05-29',
            'Durham': 'https://www.metoffice.gov.uk/weather/forecast/gcwzefp2c#?date=2024-05-29',
            'Ely': 'https://www.metoffice.gov.uk/weather/forecast/gcjsyk4mw#?nearestTo=Ely%20(Cardiff)&date=2024-05-29',
            'Exeter': 'https://www.metoffice.gov.uk/weather/forecast/gcj2x8gt4#?date=2024-05-29',
            'Gloucester': 'https://www.metoffice.gov.uk/weather/forecast/gcnrj1e0w#?date=2024-05-29',
            'Hereford': 'https://www.metoffice.gov.uk/weather/forecast/gcq04hx21#?date=2024-05-29',
            'Kingston upon Hull': 'https://www.metoffice.gov.uk/weather/forecast/gcxcb25c4#?date=2024-05-29',
            'Lancaster': 'https://www.metoffice.gov.uk/weather/forecast/gcw52qce5#?date=2024-05-29',
            'Leeds': 'https://www.metoffice.gov.uk/weather/forecast/gcwfhf1w0#?date=2024-05-29',
            'Leicester': 'https://www.metoffice.gov.uk/weather/forecast/gcr5qn5jy#?date=2024-05-29',
            'Lichfield': 'https://www.metoffice.gov.uk/weather/forecast/gcqewq76c#?date=2024-05-29',
            'Lincoln': 'https://www.metoffice.gov.uk/weather/forecast/gcrwgdr98#?date=2024-05-29',
            'Liverpool': 'https://www.metoffice.gov.uk/weather/forecast/gcmzggpxq#?date=2024-05-29',
            'Manchester': 'https://www.metoffice.gov.uk/weather/forecast/gcw2hzs1u#?date=2024-05-29',
            'Milton Keynes': 'https://www.metoffice.gov.uk/weather/forecast/gcr2nc3b7#?date=2024-05-29',
            'Newcastle upon Tyne': 'https://www.metoffice.gov.uk/weather/forecast/gcybg0rne#?date=2024-05-29',
            'Norwich': 'https://www.metoffice.gov.uk/weather/forecast/u12gmt1fz#?date=2024-05-29',
            'Nottingham': 'https://www.metoffice.gov.uk/weather/forecast/gcrjp3v96#?date=2024-05-29',
            'Oxford': 'https://www.metoffice.gov.uk/weather/forecast/gcpn7mp10#?date=2024-05-29',
            'Peterborough': 'https://www.metoffice.gov.uk/weather/forecast/gcrg49fhe#?date=2024-05-29',
            'Plymouth': 'https://www.metoffice.gov.uk/weather/forecast/gbvn9cv4h#?date=2024-05-29',
            'Portsmouth': 'https://www.metoffice.gov.uk/weather/forecast/gcp0zn6wn#?date=2024-05-29',
            'Preston': 'https://www.metoffice.gov.uk/weather/forecast/gcw1fe28j#?date=2024-05-29',
            'Ripon': 'https://www.metoffice.gov.uk/weather/forecast/gcwgvr0fn#?date=2024-05-29',
            'Salford': 'https://www.metoffice.gov.uk/weather/forecast/gcw279prq#?date=2024-05-29',
            'Salisbury': 'https://www.metoffice.gov.uk/weather/forecast/gcndx0wq3#?date=2024-05-29',
            'Sheffield': 'https://www.metoffice.gov.uk/weather/forecast/gcqzwtdw7#?date=2024-05-29',
            'Southampton': 'https://www.metoffice.gov.uk/weather/forecast/gcp185f25#?date=2024-05-29',
            'Southend-on-Sea': 'https://www.metoffice.gov.uk/weather/forecast/u10t0nxqf#?date=2024-05-29',
            'St Albans': 'https://www.metoffice.gov.uk/weather/forecast/gcpy2m1yy#?date=2024-05-29',
            'Stoke-on-Trent': 'https://www.metoffice.gov.uk/weather/forecast/gcqmw2y12#?date=2024-05-29',
            'Sunderland': 'https://www.metoffice.gov.uk/weather/forecast/gcz02e3x2#?date=2024-05-29',
            'Truro': 'https://www.metoffice.gov.uk/weather/forecast/gbumvn49q#?date=2024-05-29',
            'Wakefield': 'https://www.metoffice.gov.uk/weather/forecast/gcwcmu8w8#?date=2024-05-29',
            'Wells': 'https://www.metoffice.gov.uk/weather/forecast/gcn57f71q#?date=2024-05-29',
            'Westminster': 'https://www.metoffice.gov.uk/weather/forecast/gcpuuyzwv#?date=2024-05-29',
            'Winchester': 'https://www.metoffice.gov.uk/weather/forecast/gcp46pp1c#?date=2024-05-29',
            'Wolverhampton': 'https://www.metoffice.gov.uk/weather/forecast/gcq7pt4g5#?date=2024-05-29',
            'Worcester': 'https://www.metoffice.gov.uk/weather/forecast/gcq2vmx21#?date=2024-05-29',
            'York': 'https://www.metoffice.gov.uk/weather/forecast/gcx4zrw25#?date=2024-05-29',

            "Aberdeen": "https://www.metoffice.gov.uk/weather/forecast/gfnt07u1s#?date=2024-05-29",
            "Dundee": "https://www.metoffice.gov.uk/weather/forecast/gfjchqtgs#?date=2024-05-29",
            "Edinburgh": "https://www.metoffice.gov.uk/weather/forecast/gcvwr3zrw#?date=2024-05-29",
            "Glasgow": "https://www.metoffice.gov.uk/weather/forecast/gcuvz3bch#?date=2024-05-29",
            "Inverness": "https://www.metoffice.gov.uk/weather/forecast/gfhyzzs9j#?date=2024-05-29",
            "Perth": "https://www.metoffice.gov.uk/weather/forecast/gfj8cfqv3#?date=2024-05-29",
            "Stirling": "https://www.metoffice.gov.uk/weather/forecast/gcvpnrf34#?date=2024-05-29",
            "Bangor": "https://www.metoffice.gov.uk/weather/forecast/gcmnf1dn6#?nearestTo=Bangor%20(Gwynedd)&date=2024-05-29",
            "Cardiff": "https://www.metoffice.gov.uk/weather/forecast/gcjszevgx#?date=2024-05-29",
            "Newport": "https://www.metoffice.gov.uk/weather/forecast/gcjv7yd0v#?date=2024-05-29",
            "St Asaph": "https://www.metoffice.gov.uk/weather/forecast/gcmwcxm2d#?date=2024-05-29",
            "St Davids": "https://www.metoffice.gov.uk/weather/forecast/gchr0hwhn#?date=2024-05-29",
            "Swansea": "https://www.metoffice.gov.uk/weather/forecast/gcjjwm34p#?date=2024-05-29",
            "Wrexham": "https://www.metoffice.gov.uk/weather/forecast/gcmvgbjuw#?date=2024-05-29",
            "Armagh": "https://www.metoffice.gov.uk/weather/forecast/gcem0tkwp#?date=2024-05-29",
            "Belfast": "https://www.metoffice.gov.uk/weather/forecast/gcey94cuf#?date=2024-05-29",
            "Derry (Londonderry)": "https://www.metoffice.gov.uk/weather/forecast/gcfbc7ef2#?nearestTo=Londonderry%20(Londonderry%20(Derry))&date=2024-05-29",
            "Lisburn": "https://www.metoffice.gov.uk/weather/forecast/gcewn76zy#?date=2024-05-29",
            "Newry": "https://www.metoffice.gov.uk/weather/forecast/gcekpv7ph#?date=2024-05-29",

            "Cork": "https://www.metoffice.gov.uk/weather/forecast/gc1zr2076#?date=2024-05-29",
            "Dublin": "https://www.metoffice.gov.uk/weather/forecast/gc7x92466#?date=2024-05-29",
            "Galway": "https://www.metoffice.gov.uk/weather/forecast/gc3x1g6dq#?date=2024-05-29",
            "Kilkenny": "https://www.metoffice.gov.uk/weather/forecast/gc6gdet19#?date=2024-05-29",
            "Limerick": "https://www.metoffice.gov.uk/weather/forecast/gc3geu70g#?date=2024-05-29",
            "Waterford": "https://www.metoffice.gov.uk/weather/forecast/gc6cjzz67#?date=2024-05-29",

            "Antwerp": "https://www.metoffice.gov.uk/weather/forecast/u155kh7fp#?date=2024-05-29",
            "Bruges": "https://www.metoffice.gov.uk/weather/forecast/u1473d2pb#?date=2024-05-29",
            "Brussels": "https://www.metoffice.gov.uk/weather/forecast/u1514zps6#?date=2024-05-29",
            "Ghent": "https://www.metoffice.gov.uk/weather/forecast/u14dkvk5g#?date=2024-05-29",
            "Amsterdam": "https://www.metoffice.gov.uk/weather/forecast/u173zeb54#?date=2024-05-29",
            "Rotterdam": "https://www.metoffice.gov.uk/weather/forecast/u15pmewzy#?date=2024-05-29",
            "Utrecht": "https://www.metoffice.gov.uk/weather/forecast/u178ksezm#?date=2024-05-29",
            "Eindhoven": "https://www.metoffice.gov.uk/weather/forecast/u15udq1wd#?date=2024-05-29",
            "Tilburg": "https://www.metoffice.gov.uk/weather/forecast/u15t7jdkk#?date=2024-05-29",
            "Groningen": "https://www.metoffice.gov.uk/weather/forecast/u1kwv82hu#?date=2024-05-29",
            "Breda": "https://www.metoffice.gov.uk/weather/forecast/u15ms93kv#?date=2024-05-29",
            "Arnhem": "https://www.metoffice.gov.uk/weather/forecast/u1hpwzwpg#?date=2024-05-29",
            "Maastricht": "https://www.metoffice.gov.uk/weather/forecast/u1h1e7cs4#?date=2024-05-29",
            "Dordrecht": "https://www.metoffice.gov.uk/weather/forecast/u15qdmzug#?date=2024-05-29",
            "Copenhagen": "https://www.metoffice.gov.uk/weather/forecast/u3buvefsh#?date=2024-05-29",
            "Aarhus": "https://www.metoffice.gov.uk/weather/forecast/u1zr2rdew#?date=2024-05-29",
            "Odense": "https://www.metoffice.gov.uk/weather/forecast/u1z75vr0q#?date=2024-05-29",
            "Aalborg": "https://www.metoffice.gov.uk/weather/forecast/u4ph3xzd0#?date=2024-05-29",
            "Esbjerg": "https://www.metoffice.gov.uk/weather/forecast/u1y586105#?date=2024-05-29",
            "Kolding": "https://www.metoffice.gov.uk/weather/forecast/u1yextxhs#?date=2024-05-29",
            "Horsens": "https://www.metoffice.gov.uk/weather/forecast/u1yvzcj20#?date=2024-05-29",
            "Vejle": "https://www.metoffice.gov.uk/weather/forecast/u1yubvew3#?date=2024-05-29",

            "Berlin": "https://www.metoffice.gov.uk/weather/forecast/u33dc2uph#?date=2024-05-29",
            "Hamburg": "https://www.metoffice.gov.uk/weather/forecast/u1x0eu3p3#?date=2024-05-29",
            "Munich": "https://www.metoffice.gov.uk/weather/forecast/u281yf6ky#?date=2024-05-29",
            "Frankfurt": "https://www.metoffice.gov.uk/weather/forecast/u0yjjs0d4#?date=2024-05-29",
            "Stuttgart": "https://www.metoffice.gov.uk/weather/forecast/u0wt8cuwm#?date=2024-05-29",
            "Dortmund": "https://www.metoffice.gov.uk/weather/forecast/u1jmj4x5c#?date=2024-05-29",
            "Essen": "https://www.metoffice.gov.uk/weather/forecast/u1huqsbkz#?date=2024-05-29",
            "Leipzig": "https://www.metoffice.gov.uk/weather/forecast/u30u1gyp7#?date=2024-05-29",
            "Bremen": "https://www.metoffice.gov.uk/weather/forecast/u1qmbqzjr#?date=2024-05-29",
            "Dresden": "https://www.metoffice.gov.uk/weather/forecast/u31f2tm5v#?date=2024-05-29",
            "Hannover": "https://www.metoffice.gov.uk/weather/forecast/u1qcvxkrw#?date=2024-05-29",
            "Duisburg": "https://www.metoffice.gov.uk/weather/forecast/u1hud6913#?date=2024-05-29",

            "Warsaw": "https://www.metoffice.gov.uk/weather/forecast/u3qcnzbf7#?date=2024-05-29",
            
            "Paris": "https://www.metoffice.gov.uk/weather/forecast/u09tvnxyj#?date=2024-05-29",
            "Marseille": "https://www.metoffice.gov.uk/weather/forecast/spey4nyk6#?date=2024-05-29",
            "Lyon": "https://www.metoffice.gov.uk/weather/forecast/u05kq67em#?date=2024-05-29",
            "Toulouse": "https://www.metoffice.gov.uk/weather/forecast/sp8zzmkzu#?date=2024-05-29",
            "Nice": "https://www.metoffice.gov.uk/weather/forecast/spv0t6u3k#?date=2024-05-29",
            "Nantes": "https://www.metoffice.gov.uk/weather/forecast/gbqut4mfh#?date=2024-05-29",
            "Strasbourg": "https://www.metoffice.gov.uk/weather/forecast/u0ts2edxj#?date=2024-05-29",
            "Montpellier": "https://www.metoffice.gov.uk/weather/forecast/spdzfhvcb#?date=2024-05-29",
            "Bordeaux": "https://www.metoffice.gov.uk/weather/forecast/ezzx5n8bq#?date=2024-05-29",
            "Lille": "https://www.metoffice.gov.uk/weather/forecast/u0fpwk98k#?date=2024-05-29",
            "Rennes": "https://www.metoffice.gov.uk/weather/forecast/gbwc2wbc0#?date=2024-05-29",
            "Reims": "https://www.metoffice.gov.uk/weather/forecast/u0fbhjtn5#?date=2024-05-29",
            "Le Havre": "https://www.metoffice.gov.uk/weather/forecast/u0b1depqk#?date=2024-05-29",
            "Toulon": "https://www.metoffice.gov.uk/weather/forecast/spsjqgw47#?date=2024-05-29",
            "Angers": "https://www.metoffice.gov.uk/weather/forecast/gbrw4z1et#?date=2024-05-29",
            "Grenoble": "https://www.metoffice.gov.uk/weather/forecast/u05f160f0#?date=2024-05-29",
            "Dijon": "https://www.metoffice.gov.uk/weather/forecast/u07t4wq4b#?date=2024-05-29",
            "Brest": "https://www.metoffice.gov.uk/weather/forecast/gbsg3ffqr#?date=2024-05-29",
            "Limoges": "https://www.metoffice.gov.uk/weather/forecast/u00ufv4f4#?date=2024-05-29",
            "Tours": "https://www.metoffice.gov.uk/weather/forecast/u02mxsymn#?date=2024-05-29",
            "Perpignan": "https://www.metoffice.gov.uk/weather/forecast/spd4cg2rm#?date=2024-05-29",

            "Luxembourg City (Luxembourg)": "https://www.metoffice.gov.uk/weather/forecast/u0u65rpxp#?date=2024-05-30",
            "Ettelbruck": "https://www.metoffice.gov.uk/weather/forecast/u0u7df3hv#?date=2024-05-30",

            "Oslo": "https://www.metoffice.gov.uk/weather/forecast/u4xsvmcv8#?date=2024-05-30",
            "Bergen": "https://www.metoffice.gov.uk/weather/forecast/u4ez3w02x#?date=2024-05-30",
            "Trondheim": "https://www.metoffice.gov.uk/weather/forecast/u5r2ve44t#?date=2024-05-30",
            "Stavanger": "https://www.metoffice.gov.uk/weather/forecast/u4kp6mk6y#?date=2024-05-30",
            "Drammen": "https://www.metoffice.gov.uk/weather/forecast/u4x5zmjsf#?date=2024-05-30",
            "Kristiansand": "https://www.metoffice.gov.uk/weather/forecast/u4mdy3bsq#?date=2024-05-30",
            "Sandnes": "https://www.metoffice.gov.uk/weather/forecast/u4knf3k6n#?date=2024-05-30",

            "Zurich (Zürich)": "https://www.metoffice.gov.uk/weather/forecast/u0qjdcy3c#?date=2024-05-30",
            "Geneva (Genève)": "https://www.metoffice.gov.uk/weather/forecast/u0hqgkr8z#?date=2024-05-30",
            "Basel": "https://www.metoffice.gov.uk/weather/forecast/u0mqs6p94#?date=2024-05-30",
            "Lausanne": "https://www.metoffice.gov.uk/weather/forecast/u0k8ydht3#?date=2024-05-30",

            "Rome (Roma)": "https://www.metoffice.gov.uk/weather/forecast/sr2y7gxtj#?date=2024-05-30",
            "Milan (Milano)": "https://www.metoffice.gov.uk/weather/forecast/u0nd95ezw#?date=2024-05-30",
            "Naples (Napoli)": "https://www.metoffice.gov.uk/weather/forecast/sr60kyq6u#?date=2024-05-30",
            "Turin (Torino)": "https://www.metoffice.gov.uk/weather/forecast/u0j3nhd38#?date=2024-05-30",
            "Palermo": "https://www.metoffice.gov.uk/weather/forecast/sqc2zg91j#?date=2024-05-30",
            "Genoa (Genova)": "https://www.metoffice.gov.uk/weather/forecast/spykeh0z3#?date=2024-05-30",
            "Bologna": "https://www.metoffice.gov.uk/weather/forecast/srbj34kqj#?date=2024-05-30",
            "Florence (Firenze)": "https://www.metoffice.gov.uk/weather/forecast/spzcp9ckv#?date=2024-05-30",
            "Bari": "https://www.metoffice.gov.uk/weather/forecast/sr7czvsm7#?date=2024-05-30",
            "Catania": "https://www.metoffice.gov.uk/weather/forecast/sqdtr4svm#?date=2024-05-30",
            "Venice (Venezia)": "https://www.metoffice.gov.uk/weather/forecast/u20f805g5#?date=2024-05-30",
            "Verona": "https://www.metoffice.gov.uk/weather/forecast/u0pdrb0c0#?date=2024-05-30",
            "Messina": "https://www.metoffice.gov.uk/weather/forecast/sqg14n6qw#?date=2024-05-30",
            "Trieste": "https://metoffice.gov.uk/weather/forecast/u21g9w669#?date=2024-05-30",
            "Taranto": "https://www.metoffice.gov.uk/weather/forecast/srhq0x34f#?date=2024-05-30",
            "Brescia": "https://www.metoffice.gov.uk/weather/forecast/u0p63umwt#?date=2024-05-30",
            "Parma": "https://www.metoffice.gov.uk/weather/forecast/spzqgj6j4#?date=2024-05-30",
            "Reggio Calabria": "https://www.metoffice.gov.uk/weather/forecast/sqg0u1eyz#?date=2024-05-30",
            "Perugia": "https://www.metoffice.gov.uk/weather/forecast/sr8vhwje8#?date=2024-05-30",
            "Ravenna": "https://www.metoffice.gov.uk/weather/forecast/srbsty7j3#?date=2024-05-30"
        }
