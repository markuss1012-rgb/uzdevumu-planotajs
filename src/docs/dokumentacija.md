# Programmatūras projekta dokumentācija
## Prasību izpēte

Ikdienā skolēniem ir daudz uzdevumu, kurus viegli aizmirst vai sajaukt. Arī man bieži gadījās, ka uzdevumi bija pierakstīti dažādās vietās vai netika pierakstīti vispār.

Tāpēc radās ideja izveidot vienkāršu uzdevumu plānotāju, kur visi uzdevumi būtu vienuviet.

Mērķauditorija ir skolēni, kuri vēlas vienkārši pierakstīt un pārskatīt savus uzdevumus.

## Projekta sākotnējā izveide

Darbu pie projekta sāku ar vienkārša grafiskā loga izveidi lai pārbaudītu kā darbojas Tkinter un vai programma pareizi atveras. Šajā posmā tika izveidots tikai logs un teksta ievades lauks kur vēlāk būs iespējams ievadīt uzdevumus.

## Uzdevumu pievienošana

Nākamajā posmā programmai pievienoju  pogu “Pievienot”, kas ļauj ievadīto tekstu pievienot uzdevumu sarakstam.

## Uzdevumu dzēšana

Programmai tika pievienota poga “Dzēst” kas ļauj izdzēst izvēlēto uzdevumu no saraksta. Ja lietotājs nav izvēlējies nevienu uzdevumu programma parāda brīdinājumu.
## Datu saglabāšana un ielāde

Lai uzdevumi nepazust'u pēc programmas aizvēršanas tika pievienota saglabāšana failā. Programma automātiski saglabā uzdevumu sarakstu `tasks.json` failā pēc pievienošanas vai dzēšanas. Atverot programmu uzdevumi tiek ielādēti no šī faila.
