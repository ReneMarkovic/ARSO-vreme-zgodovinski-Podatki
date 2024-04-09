# Namen

V tej aplikaciji je predstavljena celovita rešitev za zajemanje zgodovisnkih dnevnih podatkov, ki so dostopne preko <a href="https://www.arso.gov.si/">ARSO</a>. Aplikacija omogoča avtomatiziran prenos podatkov za vse kraje, za katere ARSO drži zgodovinske podatke. Tipičen razpon podatkov je med letoma 1961 in letom 2022. Vendar je v določenih primerih to obdobje krajše oz. del podatkov tudi manjka.

# Zagon aplikacije

postavite se v mapo, kjer je projekt naložen in zaženite ukak:
```Bash
python -m venv venv
.\venv\scripts\activate
```

V naslednjem koraku preverite ali imete nameščene vse potrebne knjižice.

```Bash
pip install -r .\requirements.txt
```

Sledi še zagon kode z ukazom
```Python
python main.py
```

**Pridobivanje podatkov lahko traja tudi do 5 ur in je priporošljivo, da se izvaja v večernih urah.**

# Kraji vključeni v zajeto bazo:
<ul>
<li>BABNO_POLJE;1961</li>
<li>BELI_KRIZ;1974</li>
<li>BILJE;1962</li>
<li>BIZELJSKO;1961</li>
<li>BOHINJSKA_CESNJICA;2002</li>
<li>BRNIK_-_LETALISCE;1963</li>
<li>CELJE_-_MEDLOG;1961</li>
<li>CERKLJE_-_LETALISCE;2005</li>
<li>CRNOMELJ_-_DOBLICE;1961</li>
<li>GODNJE;1961</li>
<li>GROSUPLJE;2008</li>
<li>IVANJKOVCI;2008</li>
<li>JERUZALEM;1961</li>
<li>KOCEVJE;1961</li>
<li>KOPER;1961</li>
<li>KREDARICA;1961</li>
<li>KRVAVEC;1961</li>
<li>LENDAVA;1961</li>
<li>LESCE;1979</li>
<li>LISCA;1984</li>
<li>LJUBLJANA_-_BEZIGRAD;1961</li>
<li>MALKOVEC;1961</li>
<li>MARIBOR_-_LETALISCE;1977</li>
<li>MARIBOR_-_TABOR;1961</li>
<li>METLIKA;1981</li>
<li>MURSKA_SOBOTA_-_RAKICAN;1961</li>
<li>NOVA_GORICA;1970</li>
<li>NOVA_VAS_NA_BLOKAH;1961</li>
<li>NOVO_MESTO;1961</li>
<li>PLANINA_POD_GOLICO;1961</li>
<li>POLICKI_VRH;1961</li>
<li>PORTOROZ_-_LETALISCE;1987</li>
<li>POSTOJNA;1961</li>
<li>PREDDVOR;1991</li>
<li>RADLJE_OB_DRAVI;1961</li>
<li>RATECE;1961</li>
<li>SEVNO;1961</li>
</ul>
