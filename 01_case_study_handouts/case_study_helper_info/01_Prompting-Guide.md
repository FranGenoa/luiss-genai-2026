---
title: "Prompting Guide"
subtitle: "Wine Business Program 2026 · GenAI Workshop · same guide for every team"
---

# How to work with Copilot this afternoon

You have about two hours. The teams that do well will not be the ones who type the most. They will be the ones who **set the context once**, work in **the right order**, and then argue with the AI.

This guide is a **sequence**. Work through it top to bottom. The order is the most important thing in it.

> **One document, not three.** Everything you need about the company, the budget, the Data Pack and your market is in **your team handout** — the file named `Handout_Team-N_<Market>.md` in the folder above this one. Wherever this guide says *"your handout"*, that is the file. Wherever it says **\[market]**, write your own.
>
> | This guide says      | In your handout it is                        |
> | -------------------- | -------------------------------------------- |
> | the company brief    | section 1                                    |
> | the CEO's ask        | section 2                                    |
> | your **Market Card** | **section 3**                                |
> | the **Data Pack**    | **section 4** (your cost line is in **4.3**) |
> | the time box         | section 7                                    |
> | the deliverables     | sections 5 and 9                             |

**Where the time goes**

| <br />                    | <br />                                                                   |
| ------------------------- | ------------------------------------------------------------------------ |
| **Phases 0–5 · \~45 min** | Set up, calculate, understand the market, build and stress-test the case |
| **Phase 6 · \~45 min**    | Generate the image, build the deck                                       |
| **\~30 min**              | Rehearse and sharpen the pitch (no Copilot needed)                       |

That is the same 45 / 45 / 30 split as section 7 of your handout. **Checkpoint at 15 minutes:** one sentence on which wine and which channel. If you are past 45 minutes and still analysing, stop and start producing.

> ### Why the order matters
>
> Most teams start by researching the market, then pick a wine, then check the numbers. That is backwards, and it is how afternoons get wasted.
>
> If you research first, you will fall in love with a wine for a good-sounding reason, and then spend two hours defending it. **If you calculate first, the arithmetic eliminates options for you and half the argument in your team disappears before it starts.**
>
> So: **numbers, then market, then strategy, then story.**

***

## The anatomy of a prompt that works

Weak prompts get generic answers. The fix is almost always the same five ingredients:

| <br />          | <br />                                                            |
| --------------- | ----------------------------------------------------------------- |
| **Role**        | "Act as a \[premium importer / CFO / sceptical buyer]"            |
| **Context**     | "Using the Data Pack and the market section of my handout"        |
| **Task**        | One clear verb. Build, compare, calculate, critique, rank         |
| **Constraints** | "Maximum 25,000 bottles" · "no discounting" · "€120,000 budget"   |
| **Format**      | "As a table" · "5 bullets" · "one paragraph I could say out loud" |

**Bad:** *"Tell me about the wine market in \[market]."*
**Better:** *"Act as a premium wine importer in \[market]. Using our Data Pack, rank our three wines by how easy they would be to sell in your top channel, and give one reason each. Table format."*

Every prompt below is a starting point, not a script. **The teams that edit these will beat the teams that paste them.**

***

# PHASE 0 · Set up the session

**\~3 minutes. Do not skip this.**

Open `https://m365.cloud.microsoft/chat`. **Upload your team handout** — the single `Handout_Team-N_<Market>.md` file. It already contains the brief, the Data Pack and your market pack, so one upload is enough. Then send this first:

> ⚠ **Check section 8 of your handout before you send anything.** Teams 4 (Germany) and 5 (Brazil) have an extra instruction there, because their markets break an assumption this guide makes by default. Fold it into Prompt 1.

### Prompt 1 · Context and read-back

> You are our export strategy advisor. I have just uploaded the full brief for Tenuta Corte Aurelia, a Chianti Classico estate planning entry into **\[YOUR MARKET]**.
>
> Read it carefully. Use **only** the figures in the Data Pack (section 4) for costs, freight, duty, taxes, trade margins and exchange rates. Do not substitute your own numbers. If something is missing, ask me or flag the assumption explicitly.
>
> Before we start: summarise back to me in 5 bullets what you understand about the company, the budget, the constraints and what the CEO is actually asking for.

**Check the read-back before you continue.** It must have the budget, the three wines and their costs, your market's duty and tax line from section 4.3, and the CEO's three questions right. If Copilot has misunderstood the brief now, everything after it is wrong and **you will not notice for forty minutes**.

**Stay in this same conversation all afternoon.** A new chat forgets everything.

***

# PHASE 1 · Find out what is actually possible

**\~12 minutes. Before you research anything.**

### Prompt 2 · The table that decides your afternoon

> Using **only** the Data Pack, calculate for each of our three wines:
> (a) contribution per bottle = ex-cellar price − variable cost − €0.15 export cost;
> (b) break-even volume = €120,000 ÷ contribution per bottle;
> (c) total contribution and net result at the board's 25,000-bottle target.
>
> One table. Show the formulas.

**Stop and look at this table properly.** It is the most important output of the day. It will usually tell you that one obvious-looking option does not work at all, and that another is far stronger than you expected.

> ⚠ **If Copilot subtracts importer or distributor margin here, stop it.** Those sit *above* your ex-cellar price, in your customer's economics. They are not your cost. Your ex-cellar price is your revenue.

### Prompt 3 · Challenge the brief

> Based on that table, is the board's 25,000-bottle target realistic for the wine I was planning to lead with? Argue both sides: that the target is wrong, and that the wine choice is wrong.

Elena's targets are stated as **ambitions, not facts** (section 4.6 of your handout says so). You are allowed to tell her she is wrong. You are expected to.

> ⚠ Copilot will never volunteer this. It optimises the question you asked. You have to make it question the premise.

### Prompt 4 · Hunt for the constraint

> Check my preferred option against every constraint in my handout: total annual production for each wine in the portfolio table, our existing domestic and EU sales commitments, the €120,000 budget, and the channel rules in the market section. Is this plan physically possible?

The constraints are deliberately spread across different sections of the handout. **Nothing points them out to you**, and Copilot will not connect them unless you ask, because each number is individually reasonable.

**By the end of Phase 1 you should be able to say, in one sentence, which wine or wines you are leading with. That is the 15-minute checkpoint.**

***

# PHASE 2 · Now understand your market

**\~6 minutes. Now that you know what the numbers allow.**

### Prompt 5 · What actually matters here

> Using the market section of my handout, give me the 5 things that genuinely determine whether a small Tuscan estate succeeds or fails in \[market]. Be specific to this market, not generic wine-industry advice.

### Prompt 6 · Who buys, and where

> Who exactly buys a premium Italian red in \[market]? Describe the buyer, the occasion, and the channel they buy it in. Then tell me which of our wines fits which channel.

> **Also look at section 3.1 of your handout.** It lists three questions your market forces you to answer. They are not rhetorical — your pitch has to survive all three.

***

# PHASE 3 · Turn a price into a strategy

**\~9 minutes. This is where the strategy comes from.**

### Prompt 7 · The full price ladder

> Using **only** the Data Pack, build the price ladder for all three wines from ex-cellar to shelf price in \[market]. Show every step: freight, import duty or taxes, excise, importer +30%, distributor +25%, retail +40%, then VAT or consumer tax. Convert to local currency at the Data Pack rate. Also give the restaurant list price at 3x the distributor price. One table, three columns.

> ⚠ **Check the order of operations.** Consumption tax or VAT goes on *after* the retail mark-up, not before. Import duty goes on the landed value, *before* the trade chain. Get either backwards and the table still looks perfectly correct while the shelf price is wrong.

### Prompt 8 · The prompt almost nobody asks

> Here are our shelf prices in \[market]: \[paste them]. For each price point, tell me what a local buyer would be comparing us against at that exact price, and which channel that price naturally belongs in.

**This is usually the highest-value prompt of the afternoon.**

A price is not just an output of a calculation. It puts you next to somebody on a shelf or a wine list, and **who you end up standing next to is your positioning**, whether you chose it or not. Look hard at the numbers that come out of Prompt 7 and ask what they mean *to a buyer in your market*. Price bands, occasions, competitive sets.

Strategy that is discovered this way is defensible. Strategy that is invented before the numbers is just an opinion.

***

# PHASE 4 · Build the business case

**\~8 minutes.**

### Prompt 9 · Construct the plan

> Build a Year-1 plan totalling \[X] bottles across our wines, respecting every production ceiling. For each wine give volume, channel, contribution per bottle and total contribution. Then give blended contribution per bottle, total contribution, net result against the €120,000, ROI, and break-even volume.

### Prompt 10 · Interrogate the weakest part of your own plan

> Which component of this plan contributes least, and what is the argument for cutting it entirely? Then give me the argument for keeping it. What volume cap or channel restriction would make it safe?

***

# PHASE 5 · Risk and control

**\~7 minutes.**

### Prompt 11 · The single point of failure

> What is the single point of failure in this plan? If exactly one thing goes wrong, what takes the whole year down with it? And when in the calendar does that moment occur?

Not five risks. One. Most plans have a moment after which recovery inside Year 1 is impossible. **Finding that moment turns a vague roadmap into a plan with a real deadline**, and it is the most persuasive thing you can say to a board.

### Prompt 12 · How the numbers could lie to you

> How could this plan look successful on paper for twelve months while actually failing in \[market]? What early signal would reveal that before the financials do?

Whatever comes back is your most important **non-financial** indicator. This is a much better way to find indicators than listing plausible-sounding metrics.

### Prompt 13 · Build the indicator set

> Now give me three financial and six non-financial indicators for \[market]. For each: what we measure, the 12-month target, how often we review it, and the management action if it misses target.

> ⚠ If you cannot say what you would **do** about an indicator, it is not an indicator. It is trivia. Cut it.

### Prompt 14 · Make Copilot your opponent

**Do not skip this. It is worth more per minute than anything else you will do today.**

> Act as a sceptical, experienced importer in \[market]. I am about to pitch you. Here is my plan: \[paste it]. Tear it apart. Give me the 5 hardest questions you would ask, and tell me where you think I am kidding myself.

Then fix what it found, and **run it again** against the improved plan.

***

# PHASE 6 · Produce

**\~45 minutes. Roughly 15 on the image, 30 on the deck.**

### Prompt 15 · The positioning image

Describe the **scene**, not the object. Cover what is in frame, the setting, the mood, the light, the style, and who it is speaking to.

> Create a positioning image for a premium Chianti Classico entering \[market], aimed at \[your target buyer and channel]. \[Describe the scene, the setting, the mood and the light you want.] Style: \[photographic / editorial / illustrated]. Premium and restrained. **No text on the label. No real brand logos, use a generic DOCG seal.**

**Practical notes:**

* AI renders text badly. Ask for **no text**, or expect gibberish.
* If it refuses, it is usually a trademark issue. Remove brand references.
* Iterate: *"Same image but warmer light and a younger audience."* Do not start over.

### Prompt 16 · The deck *(switch on Think Deeper)*

> Using everything in this conversation, create a PowerPoint presentation for the CEO and the family board. Maximum 8 slides:
>
> 1. Title and our recommendation in one line
> 2. The opportunity, and why the obvious answer does not work
> 3. Pricing and margins
> 4. The Year-1 plan and the economics
> 5. Downside, base and upside
> 6. How we will know it is working
> 7. The campaign visual
> 8. The ask, including our single deadline
>
> Write it as a board pitch, not a report. Short lines, no paragraphs.

Section 9.3 of your handout gives the same eight slides with a note on what each one has to do, already worded for your market. `99_Indicative-Submission_Deck.pptx`, in this folder, is a market-neutral skeleton of them.

Download it as `.pptx` and insert your image manually.

> If no download is offered: *"Give me the deck slide by slide, with a title and maximum 5 bullets per slide, so I can paste it into PowerPoint."* **Do not lose time fighting the tool. A plain deck that exists beats a beautiful one that does not.**

***

# The last \~30 minutes · Rehearse

Close the laptop. Time the 5-minute pitch out loud, at least twice, and decide who says what. Then agree your 2-minute reflection: the prompt that worked, the thing Copilot got wrong, and the thing you would never trust it with.

**A rehearsed pitch on an average deck beats an unrehearsed pitch on a beautiful one.**

***

## When you get stuck

| Symptom                              | Fix                                                                         |
| ------------------------------------ | --------------------------------------------------------------------------- |
| Answers are vague and generic        | You gave it no role and no constraints. Add both.                           |
| It lost the plot or forgot the brief | *"Re-read the Data Pack I uploaded and confirm the figures you are using."* |
| The output is a wall of text         | *"Give me that as a table"* or *"in 5 bullets"*                             |
| It keeps agreeing with you           | Make it an opponent. Nobody learns anything from a yes-man.                 |
| The numbers changed between answers  | Pin them: *"From now on use exactly these figures: \[list them]."*          |
| Lots of output, no decision          | *"Stop giving me options. Pick ONE and defend it in five sentences."*       |
| You disagree with it                 | You are probably right. You know wine. It knows text.                       |

If none of that works, open **`02_If-You-Get-Stuck.md`** in this folder. If the problem is the arithmetic rather than the tool, go straight to its **The maths** section — contribution, the price ladder and the Year-1 total, written out step by step.

## The four mistakes teams make often

1. **Researching before calculating.** Phase 1 exists for a reason. Decide what is possible first.
2. **Accepting the first answer.** The first answer is a draft. The third answer is the work.
3. **Letting one person own the keyboard.** Rotate. The person typing is the person learning.
4. **Trusting the total.** Always check the numbers yourself.
