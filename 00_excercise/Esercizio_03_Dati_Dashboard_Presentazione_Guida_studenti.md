# Esercizio 3: dal dato grezzo alla presentazione

**Un CSV, un'analisi, una dashboard, una presentazione**

Wine Business Program 2026 | LUISS | Guida per gli studenti

## Obiettivo e risultato finale

Userete **Microsoft 365 Copilot Chat Basic** ([m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat))
per trasformare un file di dati in tre risultati successivi:

| Fase | Che cosa chiedete | Che cosa ottenete |
|---|---|---|
| 1 | Un'analisi dei dati | Un'analisi commerciale con executive summary |
| 2 | Una dashboard | Un file HTML autonomo, apribile nel browser |
| 3 | Una presentazione | Una bozza di slide per la direzione |

Il punto dell'esercizio non consiste nel produrre il file piu' bello,
ma nel verificare **se ogni passaggio conserva i dati di partenza**.
Una dashboard elegante costruita su numeri inventati e' un danno,
non un risultato.

## I dati

Il file contiene **1.500 recensioni di vini italiani** pubblicate da
Wine Enthusiast e rese disponibili come dataset pubblico.

| Colonna | Significato |
|---|---|
| `id_recensione` | Identificativo progressivo |
| `nome_vino` | Nome completo del vino recensito |
| `cantina` | Produttore |
| `regione` | Macro-area italiana, per esempio Toscana o Piemonte |
| `denominazione` | Denominazione o zona indicata nella fonte |
| `vitigno` | Vitigno o tipologia di blend |
| `annata` | Anno indicato nel nome del vino |
| `punteggio` | Voto da 80 a 100 assegnato dal recensore |
| `fascia_punteggio` | Raggruppamento del punteggio in quattro fasce |
| `prezzo_usd` | Prezzo di riferimento in dollari statunitensi |
| `fascia_prezzo_usd` | Raggruppamento del prezzo in cinque fasce |
| `recensore` | Nome del degustatore |
| `nota_degustazione` | Testo della recensione, in inglese |
| `punti_per_dollaro` | Punteggio diviso per prezzo, indicatore di rapporto qualita'-prezzo |

**Attenzione ai limiti.** I punteggi provengono da una singola rivista
statunitense e riguardano i vini che ha scelto di recensire: non sono
un campione rappresentativo della produzione italiana. I prezzi sono in
dollari e si riferiscono al mercato statunitense nel periodo della fonte,
non ai listini attuali di cantina. Un vitigno con pochissime recensioni
non consente conclusioni solide.

## Cosa serve

* Un computer con browser e connessione Internet.
* Accesso a Microsoft 365 Copilot Chat Basic con un account di lavoro
  o universitario abilitato.
* Il modello **GPT-5.6-Think** selezionato nella chat: si imposta
  al passo 2.
* Il file `vini_italiani_recensioni.csv`, scaricato prima dell'attivita'.

Non servono Excel, Power BI, strumenti di programmazione, abbonamenti
aggiuntivi o altre applicazioni AI.

**Si lavora individualmente**: ognuno al proprio computer, nella propria
chat. Guidate voi la conversazione con Copilot e siete voi a controllare
che i numeri citati esistano davvero nel file.

## Tempo: 15 minuti totali

**Prima del timer:** accesso a Copilot effettuato, modello GPT-5.6-Think
selezionato, file CSV gia' scaricato sul computer
e questa guida aperta.

| Minuti | Attivita' |
|---|---|
| 00:00-01:00 | Leggete l'obiettivo e le colonne del file. |
| 01:00-02:00 | Caricate il CSV nella nuova chat: passo 2. |
| 02:00-06:00 | Prompt 1, analisi dei dati. Leggete l'executive summary. |
| 06:00-09:00 | Prompt 2, dashboard HTML. Aprite il file. |
| 09:00-12:00 | Prompt 3, presentazione. |
| 12:00-15:00 | Controllo con la checklist e condivisione in aula. |

**Al minuto 12 fermate le generazioni.** Meglio due risultati controllati
che tre non verificati.

Se un passaggio non riesce entro il tempo previsto, proseguite con il
materiale che avete: l'esercizio funziona anche con due fasi su tre.

## Passo 1. Scaricate il file prima del timer

Il file si trova nella cartella `data/esercizio_03_dati` accanto a
questa guida:

```text
00_excercise/data/esercizio_03_dati/vini_italiani_recensioni.csv
```

1. Aprite la cartella `data/esercizio_03_dati` del repository del corso.
2. Aprite il file `vini_italiani_recensioni.csv`.
3. Usate il pulsante di download, spesso indicato come "Download raw file"
   o con l'icona della freccia verso il basso.
4. Salvate il file in una posizione che ritrovate facilmente, per esempio
   la cartella Download o la Scrivania.

Non aprite il file in Excel per modificarlo. Se lo aprite per curiosita',
chiudetelo senza salvare: una riformattazione accidentale delle colonne
puo' rendere il file illeggibile per Copilot.

Se il download non funziona, chiedete il file a un compagno oppure al
docente tramite una chiavetta o una condivisione in aula.

## Passo 2. Caricate il CSV in una nuova chat: minuti 1-2

1. Aprite <https://m365.cloud.microsoft/chat>
2. Accedete con il vostro account di lavoro o universitario abilitato.
3. Avviate una **nuova conversazione**, separata dagli esercizi precedenti.
4. **Selezionate il modello GPT-5.6-Think** nel selettore del modello,
   in alto nella conversazione oppure accanto al riquadro del messaggio.
5. Usate il pulsante "+" oppure "Aggiungi contenuto"/"Add content".
6. Scegliete il file `vini_italiani_recensioni.csv` dal vostro computer.
7. Aspettate che compaia l'anteprima o il nome del file allegato.

Il modello conta in questo esercizio piu' che negli altri. GPT-5.6-Think
ragiona piu' a lungo prima di rispondere: calcola i valori in modo piu'
affidabile, regge le tre fasi consecutive senza perdere il filo e produce
un file HTML completo invece di un abbozzo. Con un modello piu' rapido,
l'analisi tende a restare generica e la dashboard a rimanere incompleta.

Se GPT-5.6-Think non e' disponibile sul vostro account, proseguite con il
modello predefinito e segnalatelo al docente: l'esercizio resta valido,
ma aspettatevi risultati piu' sintetici e controllate i numeri con
maggiore attenzione.

**Non inviate ancora il messaggio.** Prima allegate il file, poi incollate
il prompt del passo 3 nello stesso messaggio.

Se il caricamento non parte, controllate di aver selezionato il file `.csv`
e non una cartella compressa. Se il servizio rifiuta l'allegato, in via
eccezionale seguite l'esercizio accanto a un collega il cui caricamento
e' andato a buon fine.

Restate in questa stessa conversazione per tutto l'esercizio: la dashboard
e la presentazione devono basarsi sull'analisi gia' prodotta.

## Passo 3. Prompt 1, l'analisi dei dati: minuti 2-6

Copiate tutto il blocco qui sotto nel messaggio che contiene il file,
poi inviate. Il prompt e' in inglese, ma richiede il risultato in italiano.

### Prompt 1 da copiare

```text
Act as a wine business analyst preparing a briefing for the management
team of an Italian wine consortium.

Analyse the attached CSV of 1,500 Italian wine reviews and write a
detailed analysis in Italian.

Use an EXECUTIVE-FIRST structure: lead with the conclusions, then reveal
the supporting analysis and the underlying figures. Use only the attached
file as evidence. Do not search the web and do not add market statistics
from memory.

STRUCTURE THE ANALYSIS AS FOLLOWS:

1. EXECUTIVE SUMMARY
Approximately 180 words. Include a headline capturing the strongest
evidence-supported conclusion, up to four key findings ordered by
importance, one implication for a wine business, and the most important
limitation of the data.

2. THE NUMBERS THAT MATTER
Report the core figures: number of reviews, average and median score,
score range, average and median price, price range, number of distinct
wineries, grape varieties and regions, and the vintage range covered.
State clearly which measure you used and why.

3. REGIONAL PERFORMANCE
Compare the Italian regions in the file using a compact table with
number of reviews, average score, median price and average points per
dollar. Comment only on regions with enough reviews to be meaningful,
and say explicitly which ones are too small to judge.

4. PRICE AND QUALITY
Examine the relationship between price and score. Report the correlation
if you can compute it, and describe what happens across the price bands.
Identify the wines and the price bands offering the best value, using
punti_per_dollaro. Explain why a high points-per-dollar figure is not
automatically a commercial recommendation.

5. GRAPE VARIETIES AND PRODUCERS
Identify the varieties and the wineries that stand out, by volume of
reviews and by average score. Distinguish a genuinely strong performer
from one that simply has very few reviews.

6. WHAT THE TASTING NOTES REVEAL
Summarise the recurring language in the nota_degustazione column for the
highest-scoring wines compared with the lowest-scoring ones. Treat this
as qualitative evidence, not as measurement.

7. LIMITATIONS
State what this dataset cannot establish. Cover at least: the reviews
come from a single publication and reflect its selection; prices are in
US dollars for the US market in the period of the source; the file is
not a representative sample of Italian production; small sample sizes
per variety or region; scores are subjective judgements.

8. DATA APPENDIX
Place the detailed tables here. Never invent values. Mark anything you
cannot compute as "non calcolabile dai dati forniti".

WRITING STYLE
Clear, professional Italian for a management audience. Informative
headings that state the finding, not just the topic. Do not repeat the
executive summary at the end.
```

Leggete **prima l'executive summary**. Verificate due numeri a campione: il totale delle recensioni e il numero
di recensioni della regione con piu' vini. Se un numero non torna,
annotatelo e proseguite: e' un risultato dell'esercizio, non un errore vostro.

## Passo 4. Prompt 2, la dashboard HTML: minuti 6-9

**Restate nella stessa chat.** Copilot deve poter usare sia il file
sia l'analisi appena prodotta.

### Prompt 2 da copiare

```text
Now create a polished, self-contained HTML dashboard based on the same
CSV and on the analysis you just produced.

Requirements:
- A single HTML file that works offline, with no external libraries,
  no CDN links and no internet connection required.
- Designed for a stakeholder presentation to the management of a wine
  consortium.

Include:
- Executive KPI cards: total reviews, average score, median price,
  and the best-performing region by average score.
- A chart comparing average score by Italian region.
- A chart showing the distribution of wines across the score bands.
- A chart showing the relationship between price band and average score.
- A short "Findings" section and a "Recommended actions" section,
  written in Italian for stakeholders.
- An interactive table of the wines, with filtering by region and a
  search box for the wine or winery name.
- Responsive formatting for desktop, tablet and mobile.
- Print-friendly styling so it can be saved as a PDF.

Rules:
- Use only values that come from the attached CSV. Do not invent figures.
- If a value cannot be computed, leave it out rather than estimating it.
- Write all visible labels and commentary in Italian.
- Add a visible footer stating the source of the data and its main
  limitation.

Give me the complete HTML file.
```

Scaricate o copiate il file HTML e apritelo nel browser con un doppio clic.

Controllate tre cose: i **numeri delle card** coincidono con quelli
dell'analisi del passo 3, i **filtri della tabella** funzionano davvero,
il **footer** dichiara la fonte e il limite principale.

Se la dashboard mostra un numero che non compare nell'analisi, avete
trovato il punto piu' interessante dell'esercizio: annotatelo.

## Passo 5. Prompt 3, la presentazione: minuti 9-12

Sempre nella stessa chat.

### Prompt 3 da copiare

```text
Now turn this work into a PowerPoint presentation for the board of the
wine consortium.

Audience: the board. They have ten minutes and they have not seen the
data before.

Structure, 8 to 10 slides:
1. Title slide with the subject and the source of the data.
2. The single most important message, stated as a sentence, not a topic.
3. The key figures, as a small number of large, readable values.
4. Regional performance, with the comparison table.
5. Price and quality, with the main pattern and what it means
   commercially.
6. Varieties and producers that stand out.
7. What the tasting notes suggest about high-scoring wines.
8. Limitations of the data, stated plainly.
9. Recommended next steps, separating what the data supports from what
   requires further evidence.

Rules:
- Everything in Italian.
- Every figure on a slide must come from the attached CSV.
- Each slide title must state the finding, not the topic. Write
  "[Regione X] ottiene i punteggi medi piu' alti", not "Analisi regionale".
- Maximum five bullet points per slide, one line each.
- Include speaker notes for each slide, explaining what to say and which
  figure supports it.
- Do not add images, logos or market data that are not in the file.
```

Aprite la presentazione generata e controllate **le prime tre slide**.
Verificate che il messaggio principale della slide 2 sia effettivamente
sostenuto da un numero presente nel file.

Non rifinite la grafica durante i 15 minuti: la revisione estetica
si fa dopo l'attivita'.

## Passo 6. Controllo e condivisione: minuti 12-15

Riguardate i tre risultati e preparate un intervento di 30 secondi:

```text
Il messaggio principale che ho ottenuto: ...
Il numero che lo sostiene, nella colonna ...: ...
Il punto in cui l'AI ha perso o cambiato un dato: ...
Quello che questi dati non mi permettono di concludere: ...
```

Il docente chiama due o tre studenti. **Al minuto 15 l'esercizio termina.**

### Checklist finale

* [ ] Abbiamo usato GPT-5.6-Think per tutte e tre le fasi.
* [ ] L'analisi riguarda il file caricato e non dati generici sul vino.
* [ ] L'executive summary compare subito, prima delle tabelle di dettaglio.
* [ ] Il totale delle recensioni e' coerente tra analisi, dashboard e slide.
* [ ] I numeri delle card della dashboard si ritrovano nell'analisi.
* [ ] La dashboard si apre offline e i filtri funzionano.
* [ ] Ogni titolo di slide esprime un messaggio, non un argomento.
* [ ] I limiti dei dati sono dichiarati in tutti e tre i risultati.
* [ ] Abbiamo individuato almeno un punto da verificare a mano.
* [ ] Fatti, interpretazioni e proposte restano distinti.

## Che cosa osservare davvero

Questo esercizio ha una struttura a catena: ogni passaggio usa il
risultato del precedente. E' esattamente il modo in cui il lavoro si
perde nelle aziende.

Tenete d'occhio tre fenomeni:

**La perdita del dato.** Un numero corretto nell'analisi puo' arrotondarsi
nella dashboard e diventare approssimativo nella slide. Ogni passaggio
allontana dalla fonte.

**La sicurezza crescente.** Il linguaggio tende a diventare piu' assertivo
man mano che ci si avvicina alla presentazione. Le cautele dichiarate
nell'analisi spesso scompaiono nelle slide.

**La correlazione presentata come causa.** Se prezzo e punteggio si
muovono insieme, questo non dimostra che alzare il prezzo migliori il vino
o il suo punteggio.

La responsabilita' del contenuto resta di chi presenta, non del modello.

## Se qualcosa non funziona

Durante il timer non dedicate piu' di 30 secondi a un problema tecnico.

### Il modello e' tornato a quello predefinito

Alcune interfacce ripristinano il modello predefinito quando si apre una
nuova conversazione o dopo una pausa. Controllate il selettore prima di
ogni prompt e riselezionate GPT-5.6-Think. Non ricominciate l'esercizio:
proseguite e annotate a quale fase e' cambiato il modello.

### Copilot non legge il file

Controllate che il file allegato sia il `.csv` e non una cartella
compressa. Provate a ricaricarlo in un nuovo messaggio. In alternativa
chiedete: "Descrivi le colonne e il numero di righe del file allegato",
per verificare che l'allegato sia stato effettivamente letto.

### La risposta si interrompe

Nella stessa chat scrivete: "Continua dal punto in cui ti sei interrotto,
senza ripetere le sezioni gia' completate e senza introdurre nuove fonti."

### La dashboard non si apre correttamente

Chiedete: "Riscrivi il file HTML completo in un unico blocco di codice,
senza dipendenze esterne." Salvate il contenuto in un file con estensione
`.html` e apritelo con un doppio clic.

### I numeri non coincidono tra i tre risultati

Non correggeteli a mano durante l'esercizio. Annotate la differenza:
e' il risultato piu' utile che potete portare alla discussione.

### Un numero sembra sbagliato

Chiedete: "Mostra il calcolo e le righe del file da cui hai ricavato
questo valore." Se non riesce a giustificarlo, il numero non e' utilizzabile.

## Link utili

* [Copilot Chat](https://m365.cloud.microsoft/chat)
* File dell'esercizio: `data/esercizio_03_dati/vini_italiani_recensioni.csv`
* Documentazione del file: `data/esercizio_03_dati/README.md`
* Fonte originale dei dati: recensioni Wine Enthusiast pubblicate come
  dataset pubblico, riutilizzate qui in un estratto per uso didattico.
