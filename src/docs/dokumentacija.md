# Programmatūras projekta dokumentācija
## Prasību izpēte

Ikdienā skolēniem ir daudz uzdevumu, kurus viegli aizmirst vai sajaukt. Arī man bieži gadījās, ka uzdevumi bija pierakstīti dažādās vietās vai netika pierakstīti vispār.

Tāpēc radās ideja izveidot vienkāršu uzdevumu plānotāju, kur visi uzdevumi būtu vienuviet.

Mērķauditorija ir skolēni, kuri vēlas vienkārši pierakstīt un pārskatīt savus uzdevumus.

Programmatūras prasības

### Funkcionālās prasības
- Pievienot uzdevumu
- Dzēst uzdevumu
- Atzīmēt uzdevumu kā izpildītu
- Saglabāt uzdevumus failā
- Ielādēt uzdevumus, atverot programmu

### Nefunkcionālās prasības
- Programmai jābūt vienkāršai un viegli lietojamai
- Programma darbojas Windows vidē
- Programma izstrādāta Python valodā


## Projekta sākotnējā izveide

Darbu pie projekta sāku ar vienkārša grafiskā loga izveidi lai pārbaudītu kā darbojas Tkinter un vai programma pareizi atveras. Šajā posmā tika izveidots tikai logs un teksta ievades lauks kur vēlāk būs iespējams ievadīt uzdevumus.

## Uzdevumu pievienošana

Nākamajā posmā programmai pievienoju  pogu “Pievienot”, kas ļauj ievadīto tekstu pievienot uzdevumu sarakstam.

## Uzdevumu dzēšana

Programmai tika pievienota poga “Dzēst” kas ļauj izdzēst izvēlēto uzdevumu no saraksta. Ja lietotājs nav izvēlējies nevienu uzdevumu programma parāda brīdinājumu.
## Datu saglabāšana un ielāde

Lai uzdevumi nepazust'u pēc programmas aizvēršanas tika pievienota saglabāšana failā. Programma automātiski saglabā uzdevumu sarakstu `tasks.json` failā pēc pievienošanas vai dzēšanas. Atverot programmu uzdevumi tiek ielādēti no šī faila.
## Uzdevumu atzīmēšana kā izpildīti

Tika pievienota poga “Izpildīts”, kas ļauj izvēlēto uzdevumu atzīmēt kā izdarītu. Izpildītajiem uzdevumiem priekšā parādās “✅”. Nospiežot pogu vēlreiz, atzīme tiek noņemta.
## Programmas izpildfaila izveide

tika izveidots izpildfails (.exe). 
## Projektēšana

Projektā tika izmantota pakāpeniska izstrāde, sākot ar vienkāršu programmas logu un pamazām pievienojot jaunas funkcijas.

Izstrādes soļi:
1. Programmas loga izveide
2. Uzdevumu pievienošana
3. Uzdevumu dzēšana
4. Datu saglabāšana failā
5. Uzdevumu atzīmēšana kā izpildīti
## Programmatūras projektējums

Izmantotās tehnoloģijas:
- Python
- Tkinter
- JSON fails
- GitHub

Programmas logs sastāv no:
- teksta ievades lauka
- pogām “Pievienot”, “Dzēst”, “Izpildīts”
- uzdevumu saraksta





