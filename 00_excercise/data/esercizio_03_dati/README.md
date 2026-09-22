# Dati degli esercizi

## `vini_italiani_recensioni.csv`

Usato nell'**Esercizio 3: dal dato grezzo alla presentazione**.

Estratto didattico di 1.500 recensioni di vini italiani, tratto dal
dataset pubblico delle recensioni Wine Enthusiast.

| Caratteristica | Valore |
|---|---|
| Righe | 1.500 |
| Colonne | 14 |
| Dimensione | circa 580 KB |
| Codifica | UTF-8 con BOM, compatibile con Excel su Windows |
| Annate | dal 2000 al 2016 |
| Punteggi | da 81 a 99 |
| Prezzi | da 6 a 495 dollari statunitensi |
| Cantine | 930 |
| Vitigni | 101 |

### Colonne

| Colonna | Tipo | Significato |
|---|---|---|
| `id_recensione` | intero | Identificativo progressivo |
| `nome_vino` | testo | Nome completo del vino recensito |
| `cantina` | testo | Produttore |
| `regione` | testo | Macro-area italiana |
| `denominazione` | testo | Denominazione o zona indicata nella fonte |
| `vitigno` | testo | Vitigno o tipologia di blend |
| `annata` | intero | Anno indicato nel nome del vino |
| `punteggio` | intero | Voto da 80 a 100 |
| `fascia_punteggio` | testo | Raggruppamento in quattro fasce |
| `prezzo_usd` | decimale | Prezzo di riferimento in dollari statunitensi |
| `fascia_prezzo_usd` | testo | Raggruppamento in cinque fasce |
| `recensore` | testo | Nome del degustatore |
| `nota_degustazione` | testo | Recensione in inglese, fino a 260 caratteri |
| `punti_per_dollaro` | decimale | Punteggio diviso per prezzo |

### Distribuzione per regione

| Regione | Recensioni | Punteggio medio | Prezzo mediano USD |
|---|---|---|---|
| Toscana | 467 | 89,1 | 35 |
| Piemonte | 287 | 89,9 | 48 |
| Italia nord-orientale | 181 | 88,1 | 22 |
| Veneto | 163 | 88,5 | 29 |
| Sicilia e Sardegna | 141 | 88,4 | 23 |
| Italia meridionale | 106 | 88,2 | 22 |
| Italia centrale | 98 | 87,6 | 20 |
| Lombardia | 35 | 89,1 | 35 |
| Altre zone d'Italia | 12 | 89,8 | 32 |
| Italia nord-occidentale | 10 | 87,5 | 22,5 |

### Limiti dei dati

I punteggi provengono da una singola rivista statunitense e riguardano
i vini che ha scelto di recensire: il file non e' un campione
rappresentativo della produzione italiana. I prezzi sono espressi in
dollari e si riferiscono al mercato statunitense nel periodo della fonte,
non ai listini attuali di cantina. Le regioni e i vitigni con poche
recensioni non consentono conclusioni solide.

### Come e' stato generato

Lo script `_build_dataset.py` scarica la fonte pubblica, filtra le
recensioni italiane con prezzo e punteggio disponibili, estrae l'annata
dal nome del vino, esegue un campionamento stratificato per regione e
aggiunge le colonne derivate.

```bash
cd 00_excercise/data/esercizio_03_dati
python _build_dataset.py
```

Richiede `pandas`. Il seme casuale e' fissato, quindi il risultato e'
riproducibile.

### Fonte

Recensioni Wine Enthusiast, pubblicate come dataset aperto e distribuite
tramite il progetto TidyTuesday:

<https://github.com/rfordatascience/tidytuesday/tree/main/data/2019/2019-05-28>

Estratto riutilizzato qui a soli fini didattici.
