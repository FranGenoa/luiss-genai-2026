# Esercizio 1: come si usa l'AI in Italia?

**Dai grafici a un executive summary**

Wine Business Program 2026 | LUISS | Guida per gli studenti

## Obiettivo e risultato finale

Userete Microsoft 365 Copilot Chat Basic ([m365.cloud.microsoft/chat](https://m365.cloud.microsoft/chat)) per analizzare alcune immagini
dell'Anthropic Economic Index e produrre un report in italiano.

Il report deve iniziare con un executive summary: una sintesi per un
manager, con i messaggi chiave subito in evidenza. Seguono analisi,
confronti, implicazioni per le imprese, limiti e tabelle dei dati.

Attenzione: l'Index descrive l'uso osservato di Claude. Non rappresenta
tutti gli strumenti AI, tutte le imprese italiane o il solo settore vino.
L'obiettivo non consiste nel far confermare a Copilot una conclusione
prestabilita, ma nel capire cosa dimostrano davvero le immagini.

## Cosa serve

* Un computer con browser e connessione Internet.
* Accesso a Microsoft 365 Copilot Chat Basic con un account di lavoro
  o universitario abilitato.

* Il modello **GPT-5.6-Think** selezionato nella chat: si imposta
  al passo 1.

* Gli screenshot gia' pronti della cartella `data/esercizio_01_dati`,
  scaricati prima dell'attivita': si trovano al passo 2.

Non servono un account Claude, un abbonamento Copilot aggiuntivo,
Excel, PowerPoint, strumenti di programmazione o altre applicazioni AI.

**Si lavora individualmente**: ognuno al proprio computer, nella propria
chat. Usate voi Copilot e siete voi a controllare i dati: la verifica non
e' delegabile a nessun altro.

## Tempo: 10 minuti totali

**Prima del timer:** accesso a Copilot effettuato, modello GPT-5.6-Think
selezionato, screenshot gia' scaricati sul computer
e questa guida aperta. Il docente prepara anche la versione testuale
di riserva. Non cercate nuove immagini durante l'esercizio.

| Minuti      | Attivita'                                                        |
| ----------- | ---------------------------------------------------------------- |
| 00:00-01:00 | Leggete l'obiettivo e identificate paese e grafici forniti.      |
| 01:00-02:00 | Caricate gli screenshot nella nuova chat: passo 4.               |
| 02:00-05:00 | Incollate il prompt del passo 5, inviate e leggete la sintesi.   |
| 05:00-08:00 | Controllate i numeri citati e preparate la condivisione.         |
| 08:00-10:00 | Due studenti condividono 30 secondi ciascuno; il docente chiude. |

**Al minuto 8 fermate l'analisi.** Le tabelle complete, gli approfondimenti
e le riscritture non urgenti si leggono dopo l'attivita'.

Se avete gia' scaricato le immagini, i passi 2 e 3 si svolgono prima
del timer: in aula caricate i file e andate al
[prompt da copiare](#prompt-da-copiare).

Se al minuto 5 Copilot non ha prodotto una sintesi utilizzabile, non
continuate a rigenerare: ricavate dai grafici un messaggio supportato
e un limite, dichiarando che l'analisi AI non e' stata completata.

## Passo 1. Aprite Copilot Chat prima del timer

1. Aprite <https://m365.cloud.microsoft/chat>
2. Accedete con il vostro account di lavoro o universitario abilitato.
3. Avviate una nuova conversazione, separata da eventuali esercizi
   precedenti. Cercate "Nuova chat" o "New chat".
4. **Selezionate il modello GPT-5.6-Think.** Il selettore del modello si
   trova in alto nella conversazione oppure accanto al riquadro del
   messaggio. Apritelo e scegliete **GPT-5.6-Think**.
5. Lasciate questa scheda aperta.

Usiamo GPT-5.6-Think perche' ragiona in modo piu' esteso prima di
rispondere: e' il modello piu' adatto alla lettura di grafici e alla
costruzione di un'analisi strutturata. Con un modello piu' rapido la
sintesi tende a restare superficiale.

Se il selettore non compare o GPT-5.6-Think non e' disponibile sul vostro
account, proseguite con il modello proposto per impostazione predefinita
e segnalatelo al docente: l'esercizio resta valido, ma confrontate il
risultato con quello di chi ha usato GPT-5.6-Think.

Se non riuscite ad accedere, avvisate il docente e, in via eccezionale,
seguite l'esercizio accanto a un collega che dispone dell'accesso.
Non acquistate un abbonamento e non create
un account Claude. Un account Microsoft personale non garantisce
l'accesso alla stessa esperienza Microsoft 365 Copilot Chat.

## Passo 2. Scaricate gli screenshot gia' pronti

**Prima dei 10 minuti.** Le immagini sono gia' catturate: non dovete
visitare il sito durante l'esercizio.

Si trovano nella cartella `data/esercizio_01_dati` accanto a questa guida:

```text
00_exercise/data/esercizio_01_dati/01_italia_panoramica_e_attivita.png
00_exercise/data/esercizio_01_dati/02_italia_most_distinctive.png
00_exercise/data/esercizio_01_dati/03_francia_confronto_facoltativo.png
```

1. Aprite la cartella `data/esercizio_01_dati` del repository del corso.
2. Aprite ciascuna immagine.
3. Usate il pulsante di download, spesso indicato come "Download raw file"
   o con l'icona della freccia verso il basso.
4. Salvate i file in una posizione che ritrovate facilmente, per esempio
   la cartella Download o la Scrivania.

**Copilot Chat accetta al massimo tre immagini per messaggio.**
Le due immagini dell'Italia contengono insieme tutto il necessario:
scaricate sempre 01 e 02. Aggiungete 03 solo se volete affrontare anche
il confronto con la Francia.

| Immagine | Contenuto |
|---|---|
| 01 | Italia: posizione, Usage Index, argomenti piu' frequenti e distribuzione delle attivita' |
| 02 | Italia: posizione, Usage Index e argomenti piu' distintivi |
| 03 | Francia: stessa vista dell'immagine 1, facoltativa |

Le immagini 01 e 02 riportano entrambe posizione e Usage Index: serve a
mantenere visibile il contesto del paese in ogni immagine.

Aprite le immagini prima dell'attivita' e controllate che i numeri siano
leggibili sul vostro schermo.

### Se preferite catturare le immagini voi

Non e' necessario, ma e' possibile prima dell'attivita':

1. In una seconda scheda del browser, aprite:
   <https://www.anthropic.com/economic-index#country-usage>
2. Individuate la sezione "Country usage".
3. Fate clic sul nome del paese attualmente selezionato.
4. Cercate e selezionate "Italy".
5. Controllate che il pannello riporti effettivamente "Italy", non un
   altro paese e non una vista relativa agli Stati Uniti.

Il sito pubblico non richiede un account Claude per questa consultazione.
L'aspetto e le etichette dell'interfaccia possono cambiare nel tempo,
quindi i valori live possono differire da quelli delle immagini fornite.

## Passo 3. Controllate che cosa mostrano le immagini

**Solo preparazione.** Le immagini fornite contengono gia' tutto il
necessario. Prima dell'attivita' guardatele e individuate:

* L'indice di utilizzo ("Usage Index") e la posizione in classifica:
  entrambe le immagini dell'Italia.

* Gli argomenti "Most frequent": immagine 01.
* La distribuzione delle attivita' nel grafico "How people are using
  Claude": immagine 01.

* Gli argomenti "Most distinctive": immagine 02.

L'Index non fornisce in queste viste dati su collaborazione,
augmentation/automation o utilizzo per scopi personali ed educativi.
Se un'informazione non compare nelle immagini, non inventatela: e'
un limite da dichiarare nel report.

### Confronto facoltativo

L'immagine 03 mostra la Francia con gli stessi indicatori e lo stesso
raggruppamento dell'immagine 01, quindi il confronto e' legittimo.

Ricordate che con le tre immagini caricate avete gia' raggiunto il limite
di Copilot Chat: non potete aggiungerne altre nello stesso messaggio.

Se catturate voi altre immagini, per esempio "Germany" o "Spain", usate
gli stessi indicatori, periodo, filtri e livello di dettaglio. In
particolare mantenete lo stesso raggruppamento del grafico delle
attivita': le immagini fornite usano "Group by job", indicato come
"Categorized using O*NET-SOC codes". La vista "Group by category" usa
una classificazione diversa e non si confronta con quella per professione.

Non confrontate una classifica di argomenti con una di professioni,
oppure dati di mesi diversi come se fossero lo stesso insieme.
Se usate soltanto immagini dell'Italia, il report resta utile:
Copilot deve semplicemente dichiarare i limiti del confronto.

### Cosa deve restare visibile

Nelle immagini fornite nome del paese, titolo del grafico, etichette,
valori e legenda sono gia' presenti.

Se catturate voi nuove immagini, includete gli stessi elementi. Se il
paese non entra nel ritaglio, annotatelo chiaramente accanto
all'immagine. Non lasciate solo barre o colori senza contesto.

Annotate anche il link della fonte, la data di consultazione e le date
mostrate dalla pagina. "Last updated" indica l'aggiornamento della pagina:
non equivale automaticamente al mese in cui sono stati raccolti i dati.
Se il periodo di osservazione non compare, scrivete "non indicato".

## Passo 4. Caricate gli screenshot: minuti 1-2

Nella nuova chat usate "+" oppure "Aggiungi contenuto"/"Add content"
e selezionate i file PNG scaricati al passo 2.

1. Caricate `01_italia_panoramica_e_attivita.png`.
2. Caricate `02_italia_most_distinctive.png`.
3. Solo se affrontate il confronto, caricate
   `03_francia_confronto_facoltativo.png`.
4. Aspettate che compaiano tutte le anteprime.

**Non caricate piu' di tre immagini:** Copilot Chat non le accetta.
Se il caricamento di un file viene rifiutato, controllate quante
anteprime sono gia' presenti nel messaggio.

Le etichette dei pulsanti possono variare. Se il caricamento non parte,
controllate di aver selezionato il file `.png` e non una cartella.

Non inviate ancora il messaggio: aggiungete prima le immagini e poi
il prompt del passo 5. Controllate che tutte le anteprime previste
siano presenti e che il caricamento sia terminato.

### Se preferite catturare le immagini voi, prima dell'attivita'

Su Windows premete Win + Shift + S, selezionate l'area del grafico e
incollate con Ctrl + V nel riquadro del messaggio. Incollate ogni
cattura prima di farne un'altra: una nuova cattura puo' sostituire
quella precedente negli appunti.

Su Mac premete Shift + Command + 4, selezionate l'area, poi caricate il
file salvato, di solito sulla Scrivania, con il comando di aggiunta
contenuto.

**Durante il timer non esplorate il sito.** Queste istruzioni servono
soltanto prima dell'attivita'.

Tenete chiaro l'ordine delle immagini. Se caricate i file forniti
nell'ordine indicato sopra, potete aggiungere questa descrizione:

```text
Image 1: Italy, Usage Index, Most frequent e distribuzione delle attivita'.
Image 2: Italy, Most distinctive.
Image 3: France, Usage Index, Most frequent e distribuzione delle attivita'.
```

Se non avete caricato l'immagine della Francia, togliete l'ultima riga.
Non citate viste o paesi che non avete effettivamente allegato.

Non basta incollare il link del sito: Copilot potrebbe non vedere
i grafici interattivi o il paese selezionato. In questo esercizio
le immagini sono la fonte da analizzare.

Usate esclusivamente immagini pubbliche. Non includete email, schede
private del browser, dati di clienti o documenti riservati.

## Passo 5. Copiate il prompt e generate il report: minuti 2-5

Copiate tutto il testo nel blocco "Prompt da copiare" qui sotto.
Se disponibile, usate il pulsante di copia del blocco.

Incollatelo nel messaggio che contiene gli screenshot, poi inviate.
Il prompt usa l'inglese come nelle slide, ma richiede il report in italiano.

Prima di inviare, controllate che il modello selezionato sia ancora
GPT-5.6-Think: alcune interfacce tornano al modello predefinito quando
si apre una nuova conversazione. Non servono una modalita' avanzata
o un agente: usate la normale chat.

Inviate una sola richiesta e leggete prima
l'executive summary. Il prompt completo resta invariato: i dettagli
servono per approfondire dopo, non per allungare il lavoro in aula.
Non avviate altre generazioni mentre aspettate.

### Prompt da copiare

```text
Act as an economic researcher and data analyst studying how people in
Italy use AI.

Analyse all attached screenshots from the Anthropic Economic Index.
Extract as much meaningful information as possible and write a detailed
report in Italian.

Use an EXECUTIVE-FIRST structure: lead with the conclusions and key
takeaways, then progressively reveal the supporting analysis, comparisons
and underlying data. Do not begin with methodology or extraction tables.

Review all screenshots before writing the executive summary. Use only
the images as evidence; do not search the web or add statistics from memory.

STRUCTURE YOUR REPORT AS FOLLOWS:

1. EXECUTIVE SUMMARY - WHAT A MANAGER NEEDS TO KNOW

Place this immediately at the top. Keep it approximately 200 words.

Include:
- A clear headline capturing the strongest evidence-supported conclusion.
- Up to five key takeaways, ordered by importance rather than screenshot
  order. Each should explain the finding, a supporting figure where
  available, and why it matters.
- One concise implication for Italian businesses.
- The most important limitation of the evidence.

Make this section understandable on its own. Avoid vague statements such
as "AI offers many opportunities". Do not manufacture five findings if
the images support fewer.

2. THE MAIN FINDINGS - HOW ITALIANS USE CLAUDE

Expand the executive takeaways into a coherent profile, covering whatever
the screenshots actually show:
- Usage intensity, indices and rankings.
- Most frequent and most distinctive topics.
- Tasks and business functions represented.
- Work, personal and educational use.
- Collaboration, augmentation and automation.
- Other visible measures, such as autonomy or task success.
- Surprising patterns or tensions across the images.

For each finding, use:
Finding -> supporting figures and image references -> interpretation ->
relevant qualification.

Distinguish "most frequent" from "most distinctive". A common activity
is not necessarily unusually Italian.

3. INTERNATIONAL COMPARISON - WHERE ITALY DIFFERS

Compare Italy with the countries and benchmarks visible in the images.
Use a compact table, followed by the most meaningful differences.

Show useful calculations, clearly distinguishing:
- Absolute differences.
- Percentage-point gaps.
- Relative percentage differences.
- Ratios of usage indices.

State the denominator. Compare only compatible periods, metrics,
categories and filters. Do not infer a full ranking from a partial list.

4. BUSINESS IMPLICATIONS - WHAT TO INVESTIGATE OR TEST

Explain what Italian managers could learn from the observed patterns.
Include practical examples for wine businesses, without treating national
Claude data as wine-industry-specific evidence.

Separate:
- Observed facts.
- Plausible interpretations.
- Hypotheses requiring further evidence.
- Proposed business experiments and measurable outcomes.
5. LIMITATIONS AND OPEN QUESTIONS

Explain what the screenshots cannot establish, any conflicting figures,
and what additional information would materially improve the analysis.

Important boundaries:
- Observed Claude usage is not all AI adoption in Italy.
- Task categories do not identify users' actual occupations.
- Augmentation does not prove quality or productivity.
- A usage index is not the percentage of people or companies using AI.
- Missing or suppressed values are not necessarily zero.
- A single snapshot cannot establish trends or causation.

Do not present cultural, organisational or economic explanations as
proven causes.

6. DATA APPENDIX - THE EVIDENCE BEHIND THE REPORT

Place the detailed extraction tables here, not at the beginning.

Label the screenshots Image 1, Image 2, etc. Extract all readable relevant
figures into organised tables:
metric/category | value | unit | country | period, if visible | image reference.

Preserve original labels alongside Italian explanations. Deduplicate
overlapping images and flag differences in filters or classification.
Do not sum overlapping categories.

Mark unreadable values as "non leggibile" and missing information as
"non disponibile nelle immagini". Never invent values or observation dates.

WRITING STYLE

Use clear, professional Italian suitable for a management audience.
Make headings informative: state the finding, not just the topic.
Keep the executive summary concise and the subsequent analysis thorough.
Let readers stop after the summary or continue into progressively deeper
detail. Avoid repetition and do not add another executive summary at the end.

```

## Passo 6. Condividete il risultato:

Tenete nella chat il report e gli screenshot di riferimento.
Non create slide e non esportate file durante i 10 minuti.
Potrete conservare o completare il report dopo l'attivita'.

Per la discussione preparate un intervento di 30 secondi:

```text
Il mio messaggio principale: ...
Il dato che lo sostiene, nell'immagine numero ...: ...
La cosa che questi dati non mi permettono di concludere: ...
```

Il docente chiama soltanto due studenti: 30 secondi ciascuno.
L'ultimo minuto serve alla conclusione del docente. **Al minuto 10
l'esercizio termina.** Non leggete ad alta voce l'intero report.

### Checklist finale

* [ ] Il report riguarda le immagini effettivamente fornite.
* [ ] L'executive summary compare subito, prima delle tabelle dettagliate.
* [ ] I messaggi scelti sono comprensibili anche senza leggere tutto il report.
* [ ] Ogni numero dei messaggi scelti rimanda a un'immagine leggibile.
* [ ] Nei messaggi scelti sono distinti fatti, interpretazioni e proposte.
* [ ] Non presentiamo come fatti dati o cause non supportati.
* [ ] I limiti dei dati su Claude sono dichiarati.
* [ ] Sono pronti un messaggio principale e una cautela per la discussione.
* [ ] Le parti non controllate restano una bozza per il lavoro successivo.

## Se qualcosa non funziona

Durante il timer non dedicate piu' di 30 secondi a un problema tecnico:
usate il testo di riserva gia' pronto oppure, in via eccezionale,
seguite l'esercizio accanto a un collega.
Le istruzioni di recupero qui sotto servono prima o dopo l'attivita',
non aggiungono tempo ai 10 minuti.

### Copilot non riconosce bene un grafico

Ritagliate una porzione piu' leggibile, mantenendo titolo, paese e legenda.
Caricate il nuovo ritaglio e specificate quale immagine sostituisce.
In alternativa, trascrivete voi i valori leggibili e indicate che si
tratta di una trascrizione della fonte.

### Il sito non mostra gli stessi valori delle slide

Usate valori, filtri e periodo delle vostre immagini. Non cercate di
forzare il risultato per farlo coincidere con le slide.

### Il report si interrompe

Nella stessa chat scrivete: "Continua dal punto in cui ti sei interrotto,
senza ripetere le sezioni gia' completate e senza introdurre nuove fonti."

### Il caricamento delle immagini non compare o raggiunge un limite

Copilot Chat accetta al massimo tre immagini per messaggio. Se il
caricamento viene rifiutato, togliete l'immagine della Francia e
proseguite con le due dell'Italia: contengono tutto il necessario.

Non acquistate servizi aggiuntivi. Se il problema persiste, usate le
immagini gia' accettate, seguite l'esercizio accanto a un collega abilitato
oppure seguite l'alternativa testuale qui sotto. Disponibilita' e limiti
dipendono dal servizio e dall'account.

## Alternativa testuale: solo se non potete usare gli screenshot

Questa alternativa mantiene l'analisi, ma non la lettura di immagini.
Usa una fotografia dei dati ripresa dalle slide del corso, non i valori
live del sito. Non contiene informazioni su argomenti o collaborazione.

Aprite una nuova chat, sempre con il modello GPT-5.6-Think selezionato.
Copiate il seguente blocco completo al posto del prompt lungo
e degli allegati:

```text
Analizza esclusivamente i dati forniti qui sotto e scrivi un report
in italiano. Non cercare sul web e non aggiungere statistiche dalla memoria.

Fonte 1: Anthropic Economic Index, valori riportati nelle slide del corso.
Usage Index:
Italy 1.70
France 3.97
Germany 2.40
Spain 2.69
Netherlands 3.90

Definizione: quota di utilizzo divisa per quota di popolazione in eta'
lavorativa, 15-64 anni. Il valore 1 indica un utilizzo proporzionale.
L'indice non rappresenta la percentuale di persone o imprese che usano AI.

Apri con un executive summary di circa 200 parole, o meno se i dati
non giustificano una sintesi cosi' lunga: titolo, messaggi chiave,
implicazione per un manager e limite principale.

Poi presenta, in questo ordine:
1. Analisi dei dati disponibili sull'Italia.
2. Confronti con i paesi elencati, mostrando calcoli e denominatori.
3. Una possibile implicazione per il settore vino, come ipotesi da testare.
4. Limiti e domande aperte.
5. Appendice con i dati originali, citando Fonte 1.

Le informazioni su attivita', professioni, collaborazione, automazione,
uso personale o educativo non sono fornite: dichiaralo senza inventarle.
Non costruire una classifica mondiale da questi cinque paesi.
Non confondere l'uso osservato di Claude con tutta l'adozione AI in Italia.
Non ripetere la sintesi alla fine.

```

Preparate l'intervento seguendo il passo 6 e la checklist finale.

## Link utili

* [Copilot Chat](https://m365.cloud.microsoft/chat)
* Immagini dell'esercizio: `data/esercizio_01_dati/`
* Documentazione delle immagini: `data/esercizio_01_dati/README.md`
* [Anthropic Economic Index](https://www.anthropic.com/economic-index)
* [Documentazione della release di giugno 2026](https://huggingface.co/datasets/Anthropic/EconomicIndex/blob/main/release_2026_06_26/data_documentation.md), per approfondire dopo l'attivita'.

Questa guida riguarda soltanto l'esercizio 1. I riferimenti alla release
2026 non implicano che la pagina live resti invariata nel tempo.
