---
title: "Se vi bloccate"
subtitle: "Wine Business Program 2026 · Workshop GenAI · stessa guida per tutti i team"
---

# Se vi bloccate

Aprite questo file se una delle seguenti situazioni è vera:

* Siete al checkpoint a 15 minuti e non riuscite ancora a dire quale vino e quale canale.
* Avete molto testo da Copilot e nessuna decisione.
* **I vostri numeri non tornano e non capite dove.**
* Il vostro team sta discutendo e nessuno riesce a dimostrare nulla.
* Mancano 30 minuti e non avete nulla da consegnare.

Alla fine trovate un piano di emergenza per ciascuna di queste situazioni. I calcoli sono in **La matematica**, a metà guida. Iniziate dal metodo.

> **Dove trovare le informazioni.** Tutto ciò che vi serve è nella **vostra dispensa del team**: `Handout_Team-N_<Market>.md` nella cartella sopra questa. L'azienda e il portafoglio sono nella sezione 1, la richiesta della CEO nella sezione 2, **il vostro mercato nella sezione 3**, **il Data Pack nella sezione 4** (stock disponibile in 4.2, input della vostra scala prezzi in 4.3), le consegne nelle sezioni 5 e 9.

***

## Il metodo: cinque domande, in questo ordine

L'ordine conta più di ogni altra cosa in questa guida. La maggior parte dei team si blocca perché parte dalla terza domanda.

### 1. Che cosa consentono i numeri?

**Non decidete ancora nulla. Prima calcolate.**

Prendete tutti e tre i vini. Per ciascuno, calcolate il margine di contribuzione per bottiglia, poi quante bottiglie dovreste vendere per recuperare €120.000. Fatelo prima di avere qualsiasi opinione sul vostro mercato.

Di solito scoprirete che **almeno un'opzione è aritmeticamente impossibile e almeno una è molto migliore di quanto sembri**. Quella singola tabella elimina gran parte della discussione nel team, perché sostituisce l'opinione con un vincolo.

> *"Usando solo il Data Pack, calcola per ciascuno dei nostri tre vini: margine di contribuzione per bottiglia dopo costo variabile e costo di esportazione, e numero di bottiglie necessarie per recuperare €120.000. Mostra la formula. Una tabella."*

**Poi fate la domanda che la maggior parte dei team non fa mai:** l'obiettivo del CdA di 25.000 bottiglie funziona davvero con il vino che stavate per scegliere? Gli obiettivi di Elena sono indicati nella sezione 4.6 della vostra dispensa come ambizioni, non come fatti. Potete dirle che ha torto. Ci si aspetta che lo facciate.

### 2. Che cosa vieta il brief?

Una volta trovata l'opzione più interessante, cercate il motivo per cui non potete averla.

I vincoli sono nella vostra dispensa, ma sono **deliberatamente in sezioni diverse**, quindi nulla ve li segnala. Lo stock disponibile per il nuovo mercato è nella sezione 4.2 (la produzione totale è nella tabella del portafoglio nella sezione 1). Il budget è nella lettera della CEO nella sezione 2. Le regole di canale sono nella sezione di mercato, sezione 3. Copilot non le collegherà per voi, perché ogni numero, preso singolarmente, è ragionevole.

> *"Verifica il piano che propongo rispetto a tutti i vincoli della mia dispensa: lo stock disponibile per vino nella sezione 4.2, il budget di €120.000 e le regole di canale nella sezione di mercato. Elenca tutto ciò che è impossibile o incoerente."*

Se la vostra risposta supera questa verifica, probabilmente è una risposta reale. Se non la supera, vi siete appena salvati dal presentare qualcosa che non può fisicamente accadere.

### 3. Un singolo numero significa qualcosa in questo mercato?

È qui che nasce davvero la strategia, ed è il passaggio che le persone saltano.

Costruite l'intera scala prezzi fino allo scaffale. Poi **guardate i numeri finali e chiedetevi che cosa significano per un acquirente nel vostro mercato**, non per voi. Fasce di prezzo, set competitivo, a cosa vi confronta un consumatore, che cosa un canale può e non può assortire.

> *"Ecco il nostro prezzo a scaffale in \[IL VOSTRO MERCATO] per ciascun vino. Per ognuno, dimmi a che cosa lo confronterebbe un acquirente locale a quel prezzo esatto, e a quale canale appartiene in modo naturale."*

Un prezzo non è solo un output. In ogni mercato vi mette accanto a qualcuno su uno scaffale o su una carta dei vini, e **chi vi ritrovate accanto è il vostro posizionamento**, che lo abbiate scelto o no.

### 4. Qual è l'unica cosa che farebbe fallire questo piano?

Non cinque rischi. Uno.

> *"Qual è il singolo punto di fallimento di questo piano? Se va male esattamente una cosa, qual è quella che porta con sé l'intero anno?"*

Poi chiedete quando accade. La maggior parte dei piani ha un momento dopo il quale il recupero entro l'Anno 1 è impossibile. Trovare quel momento trasforma una roadmap vaga di 12 mesi in un piano con una scadenza reale, ed è la cosa più persuasiva che possiate dire a un CdA.

### 5. In che modo i numeri potrebbero mentirci?

È così che scegliete i vostri indicatori non finanziari, ed è molto meglio che elencare metriche plausibili.

> *"In un mercato guidato dall'importatore, in che modo questo piano potrebbe sembrare un successo sulla carta per dodici mesi mentre in realtà sta fallendo? Quale segnale precoce lo rivelerebbe prima dei dati finanziari?"*

La risposta sarà il vostro indicatore non finanziario più importante. Ogni mercato ha un modo diverso di lusingarvi. Trovate il vostro.

***

## La matematica: tre calcoli, in questo ordine

**Tutti i valori sotto sono inventati a scopo illustrativo. Questi non sono i nostri vini.** Eseguite i vostri calcoli.

### 1 · Margine di contribuzione per bottiglia: il vostro punto di partenza

Solo un costo di esportazione nel Data Pack tocca il conto economico della tenuta: il costo di conformità ed etichettatura di **€0,15**. Trasporto, dazio, accisa e IVA stanno *sopra* il vostro prezzo franco cantina, perché li paga l'importatore (sezione 4.3 della vostra dispensa). Cambiano ciò che paga il consumatore, non ciò che guadagnate voi.

La sezione 4.2 riserva stock non impegnato all'interno della produzione pianificata della tenuta, senza opportunità alternative di vendita nell'Anno 1. Le vendite export non sostituiscono le vendite domestiche. Le bottiglie non acquistate dall'importatore restano in inventario e non generano alcun margine di contribuzione nell'Anno 1. I costi di produzione appartengono comunque al margine di contribuzione; lo stock non impegnato non è vino gratuito.

```
margine di contribuzione (CM) = franco cantina − costo variabile − €0,15
volume di pareggio            = €120.000 ÷ CM
risultato di mercato a V      = (V × CM) − €120.000
```

Un vino a €10,00 franco cantina che costa €6,00 da produrre:

```
CM          = 10,00 − 6,00 − 0,15        = €3,85
break-even  = 120.000 ÷ 3,85             = 31.169 bottiglie
a 25.000    = 25.000 × 3,85 − 120.000    = −€23.750
```

Fate i calcoli su tutti e tre i vini prima di avere qualsiasi opinione sul vostro mercato, poi **confrontate ogni volume di pareggio con lo stock disponibile per il nuovo mercato nella sezione 4.2 della vostra dispensa**. Un vino può avere un bellissimo volume di pareggio e comunque non esistere in quantità sufficiente. Di solito è per questo che la risposta praticabile è un **mix**.

### 2 · La scala prezzi: dove i mercati differiscono davvero

Stessa catena in ogni mercato. Cambiano solo i numeri della vostra sezione 4.3.

```
1   prezzo franco cantina
2   + trasporto e assicurazione    →  valore sbarcato (landed value)
3   × (1 + dazio all'importazione %)  il dazio si applica al VALORE SBARCATO
4   + accisa per bottiglia
5   × 1,30                         importatore
6   × 1,25                         distributore
7   × 1,40                         Retail, off-trade (vendita al dettaglio)
8   × (1 + IVA %)                  →  prezzo a scaffale
9   × tasso del vostro Data Pack   →  valuta locale (EUR/JPY 165 significa €1 = ¥165)

prezzo in carta ristorante = passaggio 6 × 3
```

Saltate il passaggio 8 negli USA (l'imposta sulle vendite è ignorata) e in Brasile (è già inclusa nel 55%). La Germania non richiede il passaggio 9.

Due errori nell'ordine delle operazioni vi danno una tabella che sembra impeccabile ed è sbagliata:
**l'IVA si applica dopo il ricarico retail, mai prima.** **Il dazio si applica al valore sbarcato, non al franco cantina.**

> **L'unica intuizione strutturale che vale la pena portare nel pitch.** I passaggi 5–7 moltiplicano tutto ciò che sta sotto di loro per **1,30 × 1,25 × 1,40 = 2,275**. Ogni €1 di costo aggiunto *prima* della filiera commerciale arriva a €2,28 sullo scaffale, prima dell'IVA. Quindi un dazio percentuale si compone con il prezzo, mentre un'accisa fissa per bottiglia è regressiva e penalizza di più il vostro vino più economico. Entrambi i fatti emergono direttamente dalla scala prezzi: non serve alcuna ricerca esterna.

### 3 · Il totale dell'Anno 1: dove i team confondono i propri numeri

```
contribuzione(vino)             = bottiglie vendute × CM(vino)
contribuzione totale            = Σ contribuzione(vino)
CM ponderato                    = contribuzione totale ÷ bottiglie totali vendute
risultato di mercato dell'Anno 1 = contribuzione totale − €120.000
ROI                             = risultato di mercato dell'Anno 1 ÷ €120.000
break-even                      = €120.000 ÷ CM ponderato
% del piano                     = break-even ÷ volume pianificato
```

**Il risultato di mercato dell'Anno 1** (chiamato anche "risultato netto" nei materiali) è il margine di contribuzione del mercato dopo le spese di lancio, non l'utile totale della tenuta né il flusso di cassa. I costi generali esistenti della tenuta, il finanziamento dell'inventario e il valore futuro dello stock invenduto sono fuori dall'esercizio. Il ROI qui è il risultato di mercato relativo al budget di lancio, non un ritorno sul capitale totale investito dalla tenuta.

**Il CM ponderato è ponderato per volume, non la media dei tre CM**, ed è valido solo per quel mix esatto. Cambiate il mix, anche in ogni scenario, e ricalcolate.

**Verifica di coerenza:** break-even × CM ponderato deve restituire €120.000. Se non lo fa, qualcosa a monte è sbagliato.

**"% del piano" è il numero che Elena ricorderà.** Dice quanta parte del piano deve funzionare per recuperare le spese di lancio su base di contribuzione, non quando si incassa. Sopra circa l'80%, state implicitamente sostenendo un'esecuzione quasi perfetta: ditelo ad alta voce prima che lo faccia lei.

> ⚠ I ricavi non sono margine di contribuzione, e nessuno dei due è utile. `Σ (volume × franco cantina)` sono ricavi. Se una slide mostra un numero grande etichettato come "utile", verificate quale grandezza sia davvero.

### Tre cose che vi faranno perdere credibilità

**I margini di importatore e distributore non sono un vostro costo.** Stanno sopra il vostro prezzo franco cantina, nell'economia del vostro cliente. Il vostro prezzo franco cantina è il vostro ricavo.

**Un piano può avere un break-even superiore al volume che spedisce.** In quel caso non può affatto raggiungere il pareggio: una conclusione molto più netta di "guadagniamo meno". Andate a cercarla nel vostro scenario pessimistico.

**Non sottraete il trasporto.** Secondo i nostri termini, l'importatore paga trasporto, dazio e accisa (sezione 4.3 della vostra dispensa), quindi appartengono alla scala prezzi, non al vostro margine di contribuzione. Se volete sostenere un accordo diverso, scrivetelo come ipotesi e ditelo nel pitch.

***

## Piani di emergenza

### "Non riusciamo a metterci d'accordo su quale vino guidare"

Smettete di discutere. Eseguite la domanda 1. L'aritmetica di solito eliminerà subito almeno un'opzione e la discussione sparirà. Se sopravvivono due opzioni, modellatele entrambe e confrontate il margine di contribuzione fianco a fianco, poi scegliete quella che si adatta meglio alla sezione di mercato della vostra dispensa. **Una decisione difesa con un numero batte una decisione difesa con un aggettivo.**

### "Abbiamo tantissimo output da Copilot ma nessuna decisione"

Gli avete chiesto di descrivere invece che di scegliere. Forzatelo:

> *"Smetti di darmi opzioni. Sulla base di tutto ciò che c'è in questa conversazione, scegli UN vino e UN canale principale per \[IL VOSTRO MERCATO] e difendi la scelta in cinque frasi. Poi dimmi l'argomento più forte contro la tua stessa scelta."*

### "Il nostro piano sembra generico"

Probabilmente lo è. Testatelo:

> *"Questo piano funzionerebbe invariato in un altro Paese? Se sì, non è una strategia per \[IL VOSTRO MERCATO]. Dimmi che cosa è generico e dammi una cosa vera solo in questo mercato."*

Poi confrontatelo con **la sezione 3.1 della vostra dispensa**. Se il vostro piano non risponde a quelle tre domande, è lì che si nasconde il generico.

### "Non riusciamo a pensare a indicatori non finanziari"

Usate la domanda 5. Poi, per ogni candidato, chiedete solo tre cose: che cosa misuriamo, che aspetto ha un buon risultato a 12 mesi, e che cosa facciamo se manca l'obiettivo. Se non sapete dire che cosa *fareste* al riguardo, non è un indicatore, è un dato irrilevante. Tagliatelo.

### "La presentazione non si costruisce"

Non combattete lo strumento. Chiedete invece il contenuto:

> *"Dammi la presentazione slide per slide. Titolo più al massimo cinque punti elenco brevi per slide, 8 slide."*

Incollate manualmente in PowerPoint: `99_Indicative-Submission_Deck.pptx` in questa cartella vi dà lo scheletro a otto slide in cui incollare. **Una presentazione semplice consegnata batte una presentazione bellissima che non esiste.**

### "Mancano 30 minuti e non abbiamo nulla"

Fate esattamente questo, in quest'ordine, e nient'altro:

1. **(5 min)** Eseguite la domanda 1. Scegliete il vino con il miglior margine di contribuzione che potete effettivamente fornire. Scrivete una frase: *"Partiamo con X attraverso il canale Y."*
2. **(8 min)** Ottenete la scala prezzi e il break-even per quel vino. Una tabella.
3. **(5 min)** Tre indicatori finanziari, tre non finanziari. Solo obiettivo e azione di attivazione.
4. **(7 min)** Chiedete a Copilot una presentazione a 8 slide dalla conversazione. Qualunque cosa esca, prendetela.
5. **(5 min)** Generate un'immagine. Primo risultato. Non iterate.

Questa è una consegna completa e difendibile. Non vincerà, ma passerà, e avrete qualcosa di reale di cui parlare nella riflessione.

***

## Tre domande che sbloccano quasi tutto

1. **"Che cosa sto assumendo qui che non ho scritto?"**
2. **"Che cosa dovrebbe essere vero perché questo sia sbagliato?"**
3. **"Se avessi un solo numero per convincere il CdA, quale sarebbe?"**

***
