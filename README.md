# Parser jpk_vat
 Prosty skrypt kompilujący przychody i wydatki w plik jpk_vat


# Jak używać
W folderze input należy umiescić 3 odpowiednio sformatowane pliki:
## info.csv
```
KodFormularza;kodSystemowy;wersjaSchemy;WariantFormularza;CelZlozenia;DataWytworzeniaJPK;DataOd;DataDo;DomyslnyKodWaluty;KodUrzedu;NIP;PelnaNazwa;REGON;KodKraju;Wojewodztwo;Powiat;Gmina;Ulica;NrDomu;NrLokalu;Miejscowosc;KodPocztowy;Poczta
```
W pliku info powinna znajdować się tylko jedna linijka
## przychod.csv
```
typSprzedazy;LpSprzedazy;NrKontrahenta;NazwaKontrahenta;AdresKontrahenta;DowodSprzedazy;DataWystawienia;DataSprzedazy;K_10;K_11;K_12;K_13;K_14;K_15;K_16;K_17;K_18;K_19;K_20;K_21;K_22;K_23;K_24;K_25;K_26;K_27;K_28;K_29;K_30;K_31;K_32;K_33;K_34;K_35;K_36;K_37;K_38;K_39
```
W pliku przychod jedna linijka odpowiada jednemu wpisowi
## wydatki.csv
```
LiczbaWierszySprzedazy;PodatekNalezny;typZakupu;LpZakupu;NrDostawcy;NazwaDostawcy;AdresDostawcy;DowodZakupu;DataZakupu;DataWplywu;K_43;K_44;K_45;K_46;K_47;K_48;K_49;K_50
```
W pliku wydatki jedna linijka odpowiada jednemu wpisowi

### Poprawnie sformatowane przykłady znajdują sie w folderze input

# Pomoc
W razie wątpliwości należy odnieść do oficjalnych instrukcji znajdujących się na [stronie Ministerstwa Finansów](http://www.finanse.mf.gov.pl/pl/pp/jpk).

# Uwaga!
Przed złożeniem wygenerowanego pliku należy sprawdzić jego poprawność.
Jest to mały projekt napisany w wolnym czasie, więc nie daje gwarancji poprawności wygenerowanego pliku jeśli zmienią się wytyczne co do formatowania.
