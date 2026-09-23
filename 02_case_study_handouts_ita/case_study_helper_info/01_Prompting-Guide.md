---
title: "Guida al Prompting"
subtitle: "Wine Business Program 2026 · Workshop GenAI · stessa guida per ogni team"
---

# Come lavorare con Copilot questo pomeriggio

Avete circa due ore. I team che lavoreranno bene non saranno quelli che scrivono di più. Saranno quelli che **impostano il contesto una volta sola**, lavorano **nell'ordine giusto** e poi discutono con l'AI.

Questa guida è una **sequenza**. Seguitela dall'inizio alla fine. L'ordine è la cosa più importante.

> **Un documento, non tre.** Tutto ciò che vi serve sull'azienda, sul budget, sul Data Pack e sul vostro mercato è nella **dispensa del vostro team**, il file chiamato `Handout_Team-N_<Market>.md` nella cartella sopra questa. Dove questa guida dice *"la vostra dispensa"*, si intende quel file. Dove dice **\[MERCATO]**, scrivete il vostro.
>
> | Questa guida dice      | Nella vostra dispensa è                      |
> | ---------------------- | -------------------------------------------- |
> | il brief dell'azienda  | sezione 1                                    |
> | la richiesta della CEO | sezione 2                                    |
> | la vostra **Scheda Mercato** | **sezione 3**                          |
> | il **Data Pack**       | **sezione 4** (stock disponibile in **4.2**, input per la vostra scala prezzi in **4.3**) |
> | la tempistica          | sezione 7                                    |
> | i risultati richiesti   | sezioni 5 e 9                                |

**Dove va il tempo**

| <br />                    | <br />                                                                   |
| ------------------------- | ------------------------------------------------------------------------ |
| **Fasi 0–5 · \~45 min** | Impostare, calcolare, capire il mercato, costruire e stress testare il caso |
| **Fase 6 · \~45 min**    | Generare l'immagine, costruire la presentazione                          |
| **\~30 min**              | Provare e affinare il pitch (Copilot non serve)                          |

È la stessa divisione 45 / 45 / 30 della sezione 7 della vostra dispensa. **Checkpoint a 15 minuti:** una frase su quale vino e quale canale. Se avete superato i 45 minuti e state ancora analizzando, fermatevi e iniziate a produrre.

> ### Perché l'ordine conta
>
> La maggior parte dei team comincia facendo ricerca sul mercato, poi sceglie un vino, poi controlla i numeri. È l'ordine contrario, ed è così che si sprecano i pomeriggi.
>
> Se fate prima la ricerca, vi innamorerete di un vino per una ragione che suona bene, e poi passerete due ore a difenderlo. **Se calcolate prima, l'aritmetica elimina opzioni per voi e metà della discussione nel vostro team sparisce prima ancora di iniziare.**
>
> Quindi: **numeri, poi mercato, poi strategia, poi storia.**

***

## L'anatomia di un prompt che funziona

I prompt deboli producono risposte generiche. La soluzione è quasi sempre negli stessi cinque ingredienti:

| <br />          | <br />                                                            |
| --------------- | ----------------------------------------------------------------- |
| **Ruolo**       | "Agisci come \[IMPORTATORE PREMIUM / CFO / ACQUIRENTE SCETTICO]" |
| **Contesto**    | "Usando il Data Pack e la sezione mercato della mia dispensa"    |
| **Compito**     | Un verbo chiaro. Costruisci, confronta, calcola, critica, classifica |
| **Vincoli**     | "Massimo 25.000 bottiglie" · "nessuno sconto" · "budget di €120.000" |
| **Formato**     | "Come tabella" · "5 punti elenco" · "un paragrafo che potrei dire ad alta voce" |

**Male:** *"Parlami del mercato del vino in \[MERCATO]."*
**Meglio:** *"Agisci come un importatore di vini premium in \[MERCATO]. Usando il nostro Data Pack, classifica i nostri tre vini in base a quanto sarebbe facile venderli nel tuo canale principale e dammi una ragione per ciascuno. Formato tabella."*

Ogni prompt qui sotto è un punto di partenza, non un copione. **I team che li modificano batteranno i team che li incollano.**

***

# FASE 0 · Impostare la sessione

**\~3 minuti. Non saltatela.**

Aprite `https://m365.cloud.microsoft/chat`. **Caricate la dispensa del vostro team**, il singolo file `Handout_Team-N_<Market>.md`. Contiene già il brief, il Data Pack e il vostro dossier di mercato, quindi basta un solo caricamento. Poi inviate questo per primo:

> ⚠ **Controllate la sezione 8 della vostra dispensa prima di inviare qualsiasi cosa.** Il Team 5 (Brasile) ha lì un'istruzione aggiuntiva, perché la sua struttura fiscale rompe un'ipotesi che questa guida usa come impostazione predefinita. Integratela nel Prompt 1.

### Prompt 1 · Contesto e riepilogo di controllo

> Sei il nostro consulente di strategia export. Ho appena caricato il brief completo per Tenuta Corte Aurelia, una tenuta di Chianti Classico che pianifica l'ingresso in **\[IL VOSTRO MERCATO]**.
>
> Leggilo attentamente. Usa **solo** le cifre del Data Pack (sezione 4) per costi, trasporto, dazi, imposte, margini commerciali e tassi di cambio. Non sostituire numeri tuoi. Se manca qualcosa, chiedimelo o segnala esplicitamente l'ipotesi.
>
> Prima di iniziare: riassumimi in 5 punti elenco che cosa hai capito sull'azienda, sul budget, sui vincoli e su ciò che la CEO sta effettivamente chiedendo.

**Controllate il riepilogo prima di continuare.** Deve riportare correttamente il budget, i tre vini e i relativi costi, la riga su dazi e imposte del vostro mercato dalla sezione 4.3, e le tre domande della CEO. Se Copilot fraintende il brief adesso, tutto ciò che viene dopo sarà sbagliato e **non ve ne accorgerete per quaranta minuti**.

Deve anche preservare l'ipotesi di stock della sezione 4.2: le bottiglie disponibili sono allocazioni non impegnate all'interno della produzione pianificata, senza vendite alternative nell'Anno 1. Le vendite export non sostituiscono clienti domestici e le bottiglie invendute restano a magazzino senza margine di contribuzione da vendite nell'Anno 1.

**Restate nella stessa conversazione per tutto il pomeriggio.** Una nuova chat dimentica tutto.

***

# FASE 1 · Scoprire che cosa è davvero possibile

**\~12 minuti. Prima di fare qualsiasi ricerca.**

### Prompt 2 · La tabella che decide il vostro pomeriggio

> Usando **solo** il Data Pack, calcola per ciascuno dei nostri tre vini:
> (a) margine di contribuzione per bottiglia = prezzo franco cantina − costo variabile − costo export di €0,15;
> (b) volume di pareggio (break-even) = €120.000 ÷ margine di contribuzione per bottiglia;
> (c) margine di contribuzione totale e risultato di mercato dell'Anno 1 dopo le spese di lancio di €120.000 al target del CdA di 25.000 bottiglie.
>
> Una tabella. Mostra le formule.

**Fermatevi e guardate bene questa tabella.** È il risultato più importante della giornata. Di solito vi dirà che un'opzione apparentemente ovvia non funziona affatto, e che un'altra è molto più forte di quanto vi aspettavate.

> ⚠ **Se Copilot sottrae qui il margine dell'importatore o del distributore, il trasporto, i dazi o le accise, fermatelo.** Questi elementi stanno *sopra* il vostro prezzo franco cantina, nell'economia del vostro cliente: l'importatore paga trasporto e imposte (sezione 4.3). Non sono un vostro costo. Il prezzo franco cantina è il vostro ricavo.

**Tenete chiara la misura.** Il risultato di mercato dell'Anno 1 è il margine di contribuzione dopo le spese di lancio, non il profitto totale della tenuta né il cash flow. Costi generali esistenti della tenuta, finanziamento dello stock e valore futuro dello stock invenduto sono fuori dall'esercizio. Mantenete i costi di produzione nella contribuzione: lo stock non impegnato non è vino gratis.

### Prompt 3 · Mettere in discussione il brief

> Sulla base di quella tabella, il target del CdA di 25.000 bottiglie è realistico per il vino con cui pensavo di partire? Argomenta entrambe le posizioni: che il target sia sbagliato, e che la scelta del vino sia sbagliata.

I target di Elena sono formulati come **ambizioni, non fatti** (lo dice la sezione 4.6 della vostra dispensa). Potete dirle che si sbaglia. Ci si aspetta che lo facciate.

> ⚠ Copilot non lo proporrà mai spontaneamente. Ottimizza la domanda che avete fatto. Dovete costringerlo a mettere in discussione la premessa.

### Prompt 4 · Cercare il vincolo

> Verifica la mia opzione preferita rispetto a ogni vincolo nella mia dispensa: lo stock disponibile per il nuovo mercato nella sezione 4.2, il budget di €120.000, le regole di canale nella sezione mercato e qualsiasi cosa esclusa dalla lettera della CEO. Questo piano è fisicamente possibile?

I vincoli sono volutamente distribuiti in diverse sezioni della dispensa. **Niente ve li segnala**, e Copilot non li collegherà se non glielo chiedete, perché ogni numero preso singolarmente è ragionevole.

**Entro la fine della Fase 1 dovreste essere in grado di dire, in una frase, con quale vino o quali vini state partendo. Questo è il checkpoint a 15 minuti.**

***

# FASE 2 · Ora capire il vostro mercato

**\~6 minuti. Ora che sapete che cosa i numeri consentono.**

### Prompt 5 · Che cosa conta davvero qui

> Usando la sezione mercato della mia dispensa, dimmi le 5 cose che determinano davvero se una piccola tenuta toscana riesce o fallisce in \[MERCATO]. Sii specifico per questo mercato, non dare generici consigli sul settore del vino.

### Prompt 6 · Chi compra, e dove

> Chi compra esattamente un rosso italiano premium in \[MERCATO]? Descrivi l'acquirente, l'occasione e il canale in cui lo compra. Poi dimmi quale dei nostri vini si adatta a quale canale.

> **Guardate anche la sezione 3.1 della vostra dispensa.** Elenca tre domande a cui il vostro mercato vi costringe a rispondere. Non sono retoriche: il vostro pitch deve reggere a tutte e tre.

***

# FASE 3 · Trasformare un prezzo in una strategia

**\~9 minuti. È qui che nasce la strategia.**

### Prompt 7 · La scala prezzi completa

> Usando **solo** il Data Pack, costruisci la scala prezzi per tutti e tre i vini dal prezzo franco cantina al prezzo a scaffale in \[MERCATO]. Mostra ogni passaggio: trasporto, dazio all'importazione o imposte, accisa, importatore +30%, distributore +25%, retail +40%, poi IVA o imposta al consumo. Converti in valuta locale al tasso del Data Pack. Indica anche il prezzo di listino ristorante a 3x il prezzo distributore. Una tabella, tre colonne.

> ⚠ **Controllate l'ordine delle operazioni.** L'imposta al consumo o l'IVA si applica *dopo* il ricarico retail, non prima. Il dazio all'importazione si applica sul valore sbarcato (landed value), *prima* della filiera commerciale. Se invertite uno dei due passaggi, la tabella sembrerà comunque perfettamente corretta mentre il prezzo a scaffale sarà sbagliato.

### Prompt 8 · Il prompt che quasi nessuno fa

> Ecco i nostri prezzi a scaffale in \[MERCATO]: \[INCOLLATE I PREZZI]. Per ciascun prezzo, dimmi contro che cosa un acquirente locale ci confronterebbe esattamente a quel prezzo, e a quale canale quel prezzo appartiene naturalmente.

**Questo è di solito il prompt a maggior valore del pomeriggio.**

Un prezzo non è solo il risultato di un calcolo. Vi mette accanto a qualcuno su uno scaffale o su una carta dei vini, e **chi vi ritrovate accanto è il vostro posizionamento**, che l'abbiate scelto o no. Guardate con attenzione i numeri che escono dal Prompt 7 e chiedetevi che cosa significano *per un acquirente nel vostro mercato*. Fasce di prezzo, occasioni, set competitivi.

La strategia scoperta in questo modo è difendibile. La strategia inventata prima dei numeri è solo un'opinione.

***

# FASE 4 · Costruire il business case

**\~8 minuti.**

### Prompt 9 · Costruire il piano

> Costruisci un piano Anno 1 per un totale di \[X] bottiglie sui nostri vini, rispettando lo stock disponibile per il nuovo mercato nella sezione 4.2. Per ciascun vino indica volume, canale, margine di contribuzione per bottiglia e margine di contribuzione totale. Poi indica margine di contribuzione medio per bottiglia, margine di contribuzione totale, risultato di mercato dell'Anno 1 dopo le spese di lancio di €120.000, ROI (risultato di mercato ÷ €120.000) e volume di pareggio (break-even). Non etichettare il risultato di mercato come profitto totale della tenuta o cash flow.

### Prompt 10 · Interrogare la parte più debole del vostro piano

> Quale componente di questo piano contribuisce meno, e qual è l'argomento per tagliarla del tutto? Poi dammi l'argomento per mantenerla. Quale limite di volume o restrizione di canale la renderebbe sicura?

***

# FASE 5 · Rischio e controllo

**\~7 minuti.**

### Prompt 11 · Il singolo punto di fallimento

> Qual è il singolo punto di fallimento in questo piano? Se va storto esattamente un elemento, che cosa trascina giù l'intero anno? E in quale momento del calendario succede?

Non cinque rischi. Uno. La maggior parte dei piani ha un momento dopo il quale recuperare entro l'Anno 1 è impossibile. **Trovare quel momento trasforma una tabella di marcia vaga in un piano con una vera scadenza**, ed è la cosa più persuasiva che possiate dire a un CdA.

### Prompt 12 · Come i numeri potrebbero mentirvi

> Come potrebbe questo piano apparire vincente sulla carta per dodici mesi mentre in realtà sta fallendo in \[MERCATO]? Quale segnale precoce lo rivelerebbe prima dei dati finanziari?

Quello che torna è il vostro indicatore **non finanziario** più importante. Questo è un modo molto migliore per trovare indicatori rispetto a elencare metriche che suonano plausibili.

### Prompt 13 · Costruire il set di indicatori

> Ora dammi tre indicatori finanziari e sei non finanziari per \[MERCATO]. Per ciascuno: che cosa misuriamo, il target a 12 mesi, con quale frequenza lo rivediamo e l'azione manageriale se manca il target.

> ⚠ Se non sapete dire che cosa **fareste** rispetto a un indicatore, non è un indicatore. È una curiosità. Tagliatelo.

### Prompt 14 · Rendere Copilot il vostro avversario

**Non saltatelo. Vale più per minuto di qualsiasi altra cosa farete oggi.**

> Agisci come un importatore esperto e scettico in \[MERCATO]. Sto per presentarti il mio pitch. Ecco il mio piano: \[INCOLLATELO]. Fallo a pezzi. Dammi le 5 domande più difficili che faresti e dimmi dove pensi che mi stia raccontando favole.

Poi correggete ciò che ha trovato, e **ripetetelo** sul piano migliorato.

***

# FASE 6 · Produrre

**\~45 minuti. Circa 15 sull'immagine, 30 sulla presentazione.**

### Prompt 15 · L'immagine di posizionamento

Descrivete la **scena**, non l'oggetto. Coprite cosa c'è nell'inquadratura, l'ambientazione, l'atmosfera, la luce, lo stile e a chi sta parlando.

> Crea un'immagine di posizionamento per un Chianti Classico premium che entra in \[MERCATO], rivolto a \[IL VOSTRO ACQUIRENTE TARGET E CANALE]. \[DESCRIVETE LA SCENA, L'AMBIENTAZIONE, L'ATMOSFERA E LA LUCE CHE VOLETE.] Stile: \[FOTOGRAFICO / EDITORIALE / ILLUSTRATO]. Premium e sobrio. **Nessun testo sull'etichetta. Nessun logo di marchi reali, usa un sigillo DOCG generico.**

**Note pratiche:**

* L'AI rende male il testo. Chiedete **nessun testo**, oppure aspettatevi parole senza senso.
* Se rifiuta, di solito è un problema di marchio. Rimuovete i riferimenti ai marchi.
* Iterate: *"Stessa immagine ma con luce più calda e un pubblico più giovane."* Non ricominciate da capo.

### Prompt 16 · La presentazione *(attivate Think Deeper)*

> Usando tutto ciò che c'è in questa conversazione, crea una presentazione PowerPoint per la CEO e il CdA familiare. 8 slide:
>
> 1. La raccomandazione: mercato, vino, canale e tre numeri chiave
> 2. Il piano ovvio, e perché lo abbiamo scartato
> 3. Che cosa paga il mercato per una bottiglia: la scala prezzi completa, fino alla valuta locale
> 4. Il piano dell'Anno 1: vino × volume × canale × margine di contribuzione, e il risultato di mercato dopo spese di lancio di €120.000
> 5. Scenari: pessimistico, base e ottimistico
> 6. Come Elena saprà che sta funzionando: indicatori, target e azioni
> 7. Il visual di posizionamento
> 8. La richiesta, inclusa la nostra singola scadenza
>
> Scrivila come un pitch per il CdA, non come una relazione. Frasi brevi, niente paragrafi.

La sezione 9.3 della vostra dispensa dà le stesse otto slide con una nota su che cosa deve fare ciascuna, già formulata per il vostro mercato. La dispensa consente fino a 10 slide se vi servono. `99_Indicative-Submission_Deck.pptx`, in questa cartella, è uno scheletro neutro rispetto al mercato.

Scaricatela come `.pptx` e inserite manualmente la vostra immagine.

> Se non viene offerto alcun download: *"Dammi la presentazione slide per slide, con un titolo e massimo 5 punti elenco per slide, così posso incollarla in PowerPoint."* **Non perdete tempo a combattere con lo strumento. Una presentazione semplice che esiste batte una bellissima che non esiste.**

***

# Gli ultimi \~30 minuti · Provare

Chiudete il laptop. Cronometrate il pitch da 5 minuti ad alta voce, almeno due volte, e decidete chi dice cosa. Poi concordate la vostra riflessione da 2 minuti: il prompt che ha funzionato, la cosa che Copilot ha sbagliato e la cosa che non gli affidereste mai.

**Un pitch provato su una presentazione media batte un pitch non provato su una bellissima.**

***

## Quando vi bloccate

| Sintomo                              | Soluzione                                                                    |
| ------------------------------------ | --------------------------------------------------------------------------- |
| Le risposte sono vaghe e generiche   | Non gli avete dato ruolo né vincoli. Aggiungete entrambi.                   |
| Ha perso il filo o dimenticato il brief | *"Rileggi il Data Pack che ho caricato e conferma le cifre che stai usando."* |
| La risposta è un muro di testo          | *"Dammelo come tabella"* oppure *"in 5 punti elenco"*                     |
| Continua a darvi ragione             | Fatene un avversario. Nessuno impara niente da una persona che dice sempre sì.                 |
| I numeri sono cambiati tra una risposta e l'altra | Fissateli: *"Da ora in poi usa esattamente queste cifre: \[ELENCATELI]."* |
| Tanta risposta, nessuna decisione      | *"Smetti di darmi opzioni. Scegline UNA e difendila in cinque frasi."*     |
| Non siete d'accordo                  | Probabilmente avete ragione voi. Voi conoscete il vino. Lui conosce il testo. |

Se niente di questo funziona, aprite **`02_If-You-Get-Stuck.md`** in questa cartella. Se il problema è l'aritmetica invece dello strumento, andate direttamente alla sua sezione **La matematica**: margine di contribuzione, scala prezzi e totale dell'Anno 1, spiegati passo per passo.

## I quattro errori che i team fanno spesso

1. **Fare ricerca prima di calcolare.** La Fase 1 esiste per una ragione. Decidete prima che cosa è possibile.
2. **Accettare la prima risposta.** La prima risposta è una bozza. La terza risposta è il lavoro.
3. **Lasciare la tastiera a una sola persona.** Ruotate. La persona che scrive è la persona che impara.
4. **Fidarsi del totale.** Controllate sempre i numeri da soli.
