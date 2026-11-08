# Measured against the Platform Cooperativism Consortium

<!-- card: The operating system, its networks and The Grove, weighed against the platform co-op movement's own principles: what we chose, why, and where we might be wrong. -->
<!-- description: The platform economy promised sharing and delivered owners who take a cut, score every worker and now sell the AI too. Here we set out what we chose for an operating system for organisations and The Grove, the first network of them, how we think it lines up with the Platform Cooperativism Consortium's ideas, and where we might be wrong. -->

*A working draft, November 2026; expect it to change. One of a series weighing what we've built against the work of networks whose ideas we respect.*

---

**In this page**

- What's being measured: an operating system, the networks of organisations running it, and The Grove, the first of them
- Our understanding of the Platform Cooperativism Consortium's ideas, which we'd welcome being corrected on
- Seven of those ideas in turn: what we chose, why, how we think it lines up, and where we might be wrong
- The places we're least sure of, for the platform co-op movement to push on

---

If you've worked anywhere near the platform co-op movement, you know how this story usually goes. A company builds an app that sits between people who do the work and people who need it done. It calls this sharing. Then it takes a cut of every job, rates every worker, changes the pay without asking, and switches people off by algorithm with no one to appeal to. The data stays with the company, and so does the value.

Now the same companies are selling AI, and AI is being bolted into the workplace. So a reader from this world should arrive with suspicions. That this is another platform with an owner in the middle, taking a cut. That a system which "helps organisations run" will watch and score the people in them. That an AI built into the work is algorithmic management with a softer voice. And that whoever owns the model owns the future of the organisations that depend on it.

This page doesn't try to argue those suspicions away. It sets out what we chose, why, and how we think it lines up with the Consortium's ideas, so that you can test our reasoning and tell us where it fails.

## What's being measured

Three things, and it helps to keep them apart.

**The operating system** is the software an organisation runs: the rules for seats, decisions, trust, money and work, with a few guardrails at its core that nobody inside an organisation can vote away. It has no name of its own. Each organisation runs its own copy.

**A network** is organisations, each running its own copy of the operating system, that recognise one another and share agreements. It's a network of operating systems, not one system everyone shares. What lets them work together is in the operating system each of them holds, and nobody owns the network. We're building towards each organisation holding its own side of everything it does with others, its services, its needs and its agreements, so that there's no network data held anywhere else. As the code stands, those still sit in one shared store; moving them into each organisation is part of what has to be built before The Grove goes live. Each network has a **Steward**: an organisation that looks after the network's code and ships its releases. The Steward isn't the network, and it holds nothing an organisation needs in order to keep running.

**The Grove** is the first such network. It's still being built and tested. At go-live, each organisation becomes its own independent DAO, running its own copy, and the Steward becomes an organisation in its own right.

One more word used below. Inside an organisation, decisions are made in **forums**. A branch is governed in one forum: the stewards of its parent and of its sibling branches, with the branch's own steward taking part as a person. The root has no parent, so it's governed by its own stewards and the stewards of the branches grown directly from it. Forums are made of people, not branches: someone holding several seats can sit in several forums, and counts once in any one of them. A forum with fewer than two distinct people passes its decisions on towards the root.

We keep to the rule the rest of the book follows: *is* only for what's built, *building towards* for what's decided but not built, and *we don't know* for what's open.

## Our understanding of the Platform Cooperativism Consortium

This is how we understand the Consortium. If we've got any of it wrong, we'd like to be corrected, and we'll change the page.

As we understand it, the Platform Cooperativism Consortium is a network and hub for cooperatively owned digital platforms, based at The New School in New York. It was launched by Trebor Scholz on 11 November 2016, at the second platform cooperativism conference, to support the cooperative platform economy through research, education, advocacy, technical support, funding coordination and events.[^1] Its research home is the Institute for the Cooperative Digital Economy, which The New School launched in 2019 with Scholz as founding director.[^2] It describes itself as "a hub that starts, grows, and converts platform coops", and it runs a resource library, a directory of platform co-ops, the Platform Co-op School and courses alongside its conferences.[^3] Its support for building co-ops has been practical as well as written: from 2018 the Platform Co-op Development Kit, begun with a $1,000,000 grant from Google.org, co-designed open-source tools and resources with pilot co-ops of care workers, waste pickers and others.[^4]

Its ideas start from Scholz's 2016 report, which set out platform cooperativism as cloning the technology of the gig economy under democratic ownership, rooted in solidarity, with innovation reframed to benefit everyone rather than a few.[^5] His later book, *Own This!*, follows co-ops that have done it, from a farmers' cooperative in southern India to a worker-owned ride service in New York.[^6]

Over the last two years the Consortium has turned towards AI. Its 2025 conference in Istanbul was called Cooperative AI, billed as "the first global conference on cooperatives and artificial intelligence"; its 2026 conference, Solidarity AI, is in Bangkok in November.[^7] We read this as a widening of the same questions, ownership, labour and governance, to data, models and compute, rather than a change of subject, but the Consortium's own news describes it as a shift in focus, and we may be reading it too neatly.[^8]

We've used seven of its ideas. The first six are among the ten principles in Scholz's 2016 report; the seventh is where the Consortium is going now:

1. **Ownership:** platforms owned collectively by the people who make most of their value.
2. **Co-determined work:** the people who work through a platform shape it, from its programming onward.
3. **Decent pay and income security:** enough to make a living, and benefits that make a living secure.
4. **Transparency and data portability:** open finances, and honesty about what data is collected, used and sold.
5. **Protection against arbitrary behaviour:** no one loses their income without warning, an explanation and a way to contest it.
6. **Rejecting excessive surveillance, and the right to log off:** no constant monitoring and ratings, and time that belongs to the worker.
7. **Cooperative AI and the solidarity stack:** AI, and everything under it, owned and governed by the communities that live with it.

The Consortium certifies nothing, so this isn't a compliance check. It's our own reading, and it may be a generous one. That's what the sections on where we might be wrong are for.

## 1. Ownership

**Our understanding.** The first principle is that platforms should be owned collectively by the people who generate most of their value.[^5] The cut that a platform owner takes, and the control that comes with owning the platform, is what platform co-ops exist to undo.

**What we chose, and why.**

- **No owner in the middle.** When one organisation provides a service to another, what it earns is its own; the Steward takes nothing from what passes between organisations. We chose this because a cut on every exchange is exactly how a platform becomes the owner of everyone else's work.
- **What an organisation holds.** We're building towards each organisation being its own unit of software on the Internet Computer, holding its own records, documents and decisions, and controlled by its own decision-making from the day it's created. Nobody will be able to push code into an organisation: adopting a release will be its own decision, by its own proposal, with a delay and a way back.[^9]
- **Who runs an organisation.** Each organisation is its own member-run body with its own purpose, money and people. An optional legal form, a DAO company owned by the organisation, which its members govern, with a purpose lock beside it, is something we're building towards, so that the law can see what the members already run.
- **Who earns from the code.** The Steward charges for its own services, setting organisations up, its own starter packs and the plan an organisation pays for, with a margin on top. That margin pays real costs: maintaining the code, testing it, the computing it runs on, and training and testing the models the operating system uses. How large the margin should be is open. Any organisation can offer starter packs and services to others, at any price, including free.
- **Who can't buy a say.** Trust and money are kept apart, with no way to turn one into the other, so money can fund the work but never buy a voice. That's one of the guardrails in the operating system's core, which no organisation can vote away, not even unanimously.[^10]

**How we think it lines up.** Closely on the cut: there's no platform owner taking one. Less closely on the platform itself. Each organisation owns its records and its members run it, but the operating system they run is looked after by the Steward, and its code is sealed.

**Where we might be wrong.** Every organisation carries its own copy of the code, freely, and can take it with it, but it can't read or change that code until it forms a network of its own. Until then, it runs rules it can't inspect, and that may feel like a kind of half-ownership, the very thing this movement warns about. The Steward will be an organisation like any other, governed by its own members, but those members aren't the organisations that depend on it. A margin is a risk, and a paid guard can grow fond of being paid.

## 2. Co-determined work

**Our understanding.** Scholz asks that the people who work through a platform be involved "from the moment of the programming of the platform" and all along its use.[^5] Democratic governance isn't only a vote on the board; it's a hand in how the tool itself works.

**What we chose, and why.**

- **The shape of the work is the members' own.** Inside an organisation, the structure changes only by proposal: branches, their purposes and accountabilities, budgets, pay. Any member can give advice on any proposal; it's actively asked of those the change affects and those with proven skill in what it touches; and the people seated in the forum decide by consent, meaning nobody there holds a reasoned objection.[^11]
- **How the work is done is written down by the people who do it.** Playbooks are plain documents, written with the people who do the work, saying how a kind of work is done here, and its people can read and change them. When a steward corrects Wise-Eye, the organisation's AI, it proposes what the organisation should take from that, and a person accepts, edits or dismisses it.[^12]
- **The code is the Steward's to write.** An organisation whose tension becomes part of a release can be credited for it; organisations are credited, never people. Adopting a release will be the organisation's own decision. But the operating system's code isn't open source, and on The Grove only a few people, seated for the purpose, can read it. We sealed it for two reasons: a system built to stop people being bossed has to be hard to strip of its guardrails and resell, and every party holding the source is another way in.

**How we think it lines up.** Strongly over an organisation's own shape and practice: the people who do the work decide how it's organised, and the AI learns from them rather than the other way round. Partly over the software: an organisation can push a tension upward, and will be able to refuse a release, but it doesn't write the code.

**Where we might be wrong.** Members sense and advise; only seat holders propose and decide, and their weight in a decision is the trust their peers have given them. That isn't one member, one vote, and a co-op reader may see it as less democratic, not more. And the people who use the operating system every day have no seat in how it's written. A tension can travel up; what goes into a release is still the Steward's call.

## 3. Decent pay and income security

**Our understanding.** Workers need pay, and benefits, enough to make a living.[^5] The gig economy's harm wasn't only low rates: it was income that could change or vanish from one week to the next.

**What we chose, and why.** The operating system never holds or moves an organisation's money. It reads the organisation's own books and governs how that money is allocated. Recorded income lands in a shared purse, the commons, not with the branch that earned it, and is allocated by need. Pay shares a period's earnings by weights the organisation sets for itself, by proposal: hours given, seats held, contribution as the organisation's own peers see it, and equal shares. Revenue booked to a branch is never a basis for pay, so the people who care, sense and hold the work aren't starved by those whose work happens to show up as income.

Under it sits a floor: an equal amount for each member each period, never earned by work, set by proposal and starting at nothing. As built, the floor comes from each period's profit, so a lean month can leave it empty; we're changing it to come from what the organisation has free, capped so it can never pay out more than is there. A floor beyond any forum's vote isn't built.

We chose to leave the size of pay to each organisation because a system that set wages would be the platform owner by another name.

**How we think it lines up.** In shape: pay is decided by the people who share it, and the quiet work counts. On security, only as far as each organisation chooses.

**Where we might be wrong.** Nothing here guarantees anyone a living. The floor starts at nothing, and an organisation can leave it there. Contribution as peers see it becomes something worth gaming once it carries any share of pay. And the principle of portable benefits, protection that moves with a worker between jobs, has no answer here at all: the operating system carries nothing for a person from one organisation to the next.

## 4. Transparency and data portability

**Our understanding.** A co-op discloses its finances, and is clear about what data it collects, how it uses it, and whom it sells it to; and people can take their data with them.[^5]

**What we chose, and why.**

- **Open books inside.** The books are open to every member: anyone can read them, every loan and what's free to spend, and money recorded on someone's word is open to question for a week. Proposals, the advice given on them and Wise-Eye's own advice sit on the open record. Branch documents are open to every member unless they're in a locked domain.
- **Openness outside is each organisation's choice.** We're building towards each organisation choosing how far anyone in the network can explore and read it, for the whole organisation and branch by branch, up to and including its books. Some of it is already there: a branch can publish what it keeps to the open web, or to named partners with a key.
- **What leaves.** An organisation can choose to share its pattern with the Steward. No text leaves: not its purpose, accountabilities, practices or measures, and nothing anyone has written. The pattern carries only the general shape of the organisation and the general kind of work it does. We're building towards this.
- **What's kept about people.** What belongs to a person is sealed, encrypted so the system can't read it: their own notes, a branch's board, and their conversation with Wise-Eye, which they can have forgotten. About people outside, the front desk keeps only the contacts they've proved, the name they gave and their cases, for a rolling year, and anyone can ask to be forgotten.[^13]
- **Portability for organisations.** Callers, cases, settings and transcripts live in the organisation's own space, so an organisation that leaves the network loses nothing. An organisation can detach and run alone, and its DNA, its purpose, documents, playbooks and decisions, goes with it if it divides.

**How we think it lines up.** Strongly inside an organisation. Across a network, as open as each organisation chooses. On data, we've tried to keep less rather than promise to share more.

**Where we might be wrong.** Portability, as we've built it, is for organisations, not for people. What a member ought to carry with them when they leave, a record of what they did or the trust they'd been given, we don't know. Openness left to each organisation may mean most choose little of it. And the code that handles all of this is sealed, so members are asked to trust rules about their data that they can't read.

## 5. Protection against arbitrary behaviour

**Our understanding.** Nobody should lose their income without warning or a way to contest it, and workers should be able to reach the people running the platform and get an explanation.[^5] The target is arbitrary discipline and deactivation by algorithm.

**What we chose, and why.**

- **No boss, no operator.** There's nobody above the rules to act arbitrarily. Structure, seats, budgets and pay change only by proposal, decided by consent in a forum. A concern, an objection saying what has to be answered first, holds a proposal until it's reworked or its author lifts it; still standing after ten days, the proposal lapses. A high-impact change waits three days before it takes effect, and a concern raised in that time stops it. Anyone can step down from a seat.
- **No decision by machine.** Wise-Eye has no seat, no vote and no trust anyone can place in it. There's no tool for consenting to a proposal and no tool for raising a concern: not a forbidden one, none. It prepares what carries a person's word, an invitation, a proposal, money in or out, and nothing happens until a person presses it. Every call it makes is checked by the system against the playbook it loaded, whatever the model says.[^12] The front desk never decides anything or changes the organisation's shape.[^13]
- **A record and a reason.** Every proposal carries the tension it starts from and the exact change it makes, so an explanation is part of the decision rather than something asked for afterwards. Four weeks after a change, by default, everyone who took part is asked whether it landed.
- **What people depend on.** Anyone who depends on something the organisation holds goes on record, and a proposal to part with it can't conclude without saying how each of them will land.

**How we think it lines up.** Closely on the algorithm: nothing automatic can take anyone's seat, pay or place. Closely on explanation. The protection rests on peers rather than on a contract.

**Where we might be wrong.** Peers can be arbitrary too. Weight in a forum is the trust peers give, so a well-liked majority can carry a change, and the person it lands on may hold one seat among several. There's no body outside the organisation to appeal to. And a record of who depends on what checks that a landing is attached, not that it's good enough.

## 6. Rejecting excessive surveillance, and the right to log off

**Our understanding.** Constant monitoring, screenshots and ratings are undignified, and workers need time to rest, learn and take part in civic life.[^5]

**What we chose, and why.**

- **No scores on people.** The operating system's reading of how work moves has no place for a person in it. Reputation, a picture of skill in each kind of matter, decides who is asked for advice, never the decision, and each person sees only their own. A branch's reading of how it's doing is said in words and never ranked. Wise-Eye never counts, ranks or pushes anyone by their numbers, and we rehearse it against being asked for a tally of who does least.[^12] People outside get no notes, tags or scores either.[^13]
- **Somewhere off the record.** The Clearing is the space for being together without an agenda. Nothing said there is kept or read.
- **Nothing pushed.** What's unattended comes into view a step at a time, never by alert. What's due shows in each person's Your day, never outside the organisation. The few plain lines Wise-Eye prepares each morning wait to be read. Even when a customer is waiting on the line, nothing is pushed to anyone's phone.

We chose this because a system that routes work can very easily become a system that measures people, and the second undoes everything self-management is for.

**How we think it lines up.** Closely: no ratings, no alerts, and a place that's off the record.

**Where we might be wrong.** No scores isn't the same as no record. Wise-Eye reads what arrives and writes each branch's documents as the work goes; a step at risk is said in the branch above; hours given can be a weight in pay, and how those hours are known isn't set out yet. Each of these is about work, not people, but a person can still feel watched by a system that remembers so much. Reputation is private, yet it quietly steers who is asked. And not pushing isn't the same as a right to log off: a place where what's due is always there to see can still pull.

## 7. Cooperative AI and the solidarity stack

**Our understanding.** The Consortium now asks how AI can be governed by cooperative principles, and how co-ops can use, build and teach it.[^14] Scholz's answer is the Solidarity Stack: cooperative data centres instead of hyperscale clouds, AI co-ops, tech co-ops, federated infrastructure and small language models, each rooted in its own community and linked to the rest.[^15] Behind it sits a question he put plainly at Istanbul, "Who owns the infrastructure of AI?", and a reminder that "AI is built on human labor", much of it hidden in the Global South.[^16] The 2026 conference frames the choice as AI governed by distant centres of power or AI shaped by the communities that live with its effects.[^7] And the Consortium's fellows are testing AI inside co-op governance itself, alert to what it may cost: one study of large co-ops asks whether language models can lift members' participation, and names the risk of depending on big AI companies' infrastructure.[^17]

**What we chose, and why.** On The Grove, AI isn't an add-on. The operating system is itself an agentic system, and Wise-Eye is part of how an organisation runs from the day it's planted.[^12]

- **Whom it serves.** Each time a person takes a seat, a companion is placed beside them, acting for that branch and that person, told every time whose behalf it's on. What comes from outside, an email or a web page, is material to work with, never an instruction.
- **What it may do alone.** Out of the box, only what stays inside: reading, routing, filing, drafting. Anything that goes out waits for a person. Its standing to act alone is earned one kind of work at a time: after five low-stakes drafts of a kind go out unedited, it offers, and a person says yes or no. One in ten of its solo calls is checked by a person, and a wrong one takes the standing away. High stakes, money, legal matters and complaints are always held for people, and a public post is only ever drafted.
- **What it learns, and whose it is.** It learns about this one organisation, and what it learns is written into the organisation's playbooks, in its own words, where its people can read and change it.
- **At the door.** The front desk is a different voice, which says first that it's an AI and that a person can take it from here. It's off until the organisation turns it on, and it finishes only what's like promises the branch has already kept.[^13]
- **The model and its keys.** Wise-Eye is a large model, reached through a thin relay outside the system that adds the key, passes the call along and keeps nothing; the keys are never in the system. Every message and model call goes on the organisation's own meter. Beneath it, we're building towards something smaller: the organisation's own sense of itself, a small learned model that senses and never acts.
- **The ground it runs on.** The operating system runs on the Internet Computer, because no one party can switch an organisation's software off there. It's governed by a vote of those who've staked its token, which can't reach into an organisation's own decisions. We'd be open to running on co-operatively owned hosting instead, or as well, if it held to the same test: that no one party, the host included, can switch an organisation off.

We chose this because the usual ways cost too much: an assistant in every tool acting for nobody in particular, or no AI at all and the admin left on whoever cares most. AI can carry the load while people keep the say.

**How we think it lines up.** Closely on governance: inside an organisation, the AI acts for named people, earns and loses its standing by evidence, and has no voice in what's decided. Not yet on ownership: the stack under it isn't held by the organisations that use it.

**Where we might be wrong.** The large model that does most of the work isn't owned by anyone on The Grove, and each call carries the words of its prompt out of the organisation to reach it. The labour and energy behind that model aren't ours to govern, and we haven't asked whose they are. Much of what keeps Wise-Eye in its place is words, which hold only as long as the model listens. The streak that earns its standing might mean five good drafts, or a tired person pressing yes without reading. And an AI built into every organisation from the start may create a dependence of its own, on the Steward's playbooks and on the models it chooses, that a co-op would want to own.

## Where things stand

| The idea | How we think it lines up |
|---|---|
| Ownership | Closely on the cut: the Steward takes nothing from what passes between organisations. Organisations own their records and carry their own copy of the code, free but sealed until they form a network of their own. |
| Co-determined work | Strongly over an organisation's own shape and playbooks. Partly over the software: an organisation can raise a tension and, from go-live, refuse a release, not write the code. |
| Decent pay and income security | In shape: pay set by those who share it, and a floor. Nothing guarantees a living, and nothing is portable. |
| Transparency and data portability | Open books inside; outside, as open as each organisation chooses. Portable for organisations, not yet for people. |
| Protection against arbitrary behaviour | Closely: nothing automatic decides, and every change carries its reason. The protection rests on peers, with nobody outside to appeal to. |
| No surveillance, and the right to log off | Closely: no scores, no alerts, a place off the record. Still, a great deal is remembered. |
| Cooperative AI and the solidarity stack | Closely on how AI is governed inside an organisation. Not yet on who owns the model or the ground it runs on. |

## Where we're least sure

None of this is a platform co-op, and we don't claim it is. These are the choices we're least sure of. We'd rather you pushed on our reasoning than took our word for it.

1. **Records owned, code sealed.** We sealed the code to protect its guardrails from capture. Organisations own what they make and carry the system with them for free, but they can't read or change it until they form a network of their own. Running rules you can't inspect may be the half-ownership this movement has spent a decade arguing against.
2. **Seats, not one member, one vote.** We chose decisions by consent among those seated, weighted by the trust their peers give them, so that the people closest to the work decide. A co-op's members may want an equal vote, and our way may leave them with too little of one.
3. **Pay left to each organisation.** We kept the operating system out of setting pay so that it could never become the owner by another name. The floor starts at nothing, and nothing here makes anyone's living secure.
4. **Portability for organisations, not people.** An organisation can leave with everything. A person leaving takes nothing with them, and we don't know what they ought to.
5. **A model nobody here owns.** Wise-Eye runs on a large model reached from outside, with the work's words carried out to it on each call. A small model of each organisation's own is something we're building towards; the large one isn't cooperative, and we haven't found one that is and does the job.
6. **The Steward's margin.** Without it there's no Steward to guard the code. With one network and one Steward, the cost of leaving that's meant to keep the margin honest is mostly theoretical for now.

And if we've misread the Platform Cooperativism Consortium's ideas anywhere on this page, please tell us. We'd rather be corrected than be generous to ourselves.

If you'd like to go further, these chapters say more: [Chapter 6, Why an operating system](why-an-operating-system.md), on the guardrails and the Internet Computer; [Chapter 11, Making decisions](making-decisions.md), on proposals, advice and consent; [Chapter 12, Trust](trust.md), on trust, reputation and why neither can be bought; [Chapter 16, The front desk](the-front-desk.md), on the AI at the organisation's door; [Chapter 17, Money and value](money-and-value.md), on the commons, the floor and pay; [Chapter 22, The co-pilot](the-co-pilot.md), on Wise-Eye and how its standing is earned and lost; [Chapter 23, Memory](memory.md), on what's sealed and what's off the record; and [Chapter 27, DNA, the network, and why not open source](dna-the-network-and-open-source.md), on the sealed code and the Steward.

---

## Notes and further reading

[^1]: Shareable, "International Consortium Launched at Second Platform Cooperativism Conference" (November 2016), shareable.net.
[^2]: The New School, "The New School Announces the Launch of The Institute for the Cooperative Digital Economy", press release, 7 May 2019, newschool.edu. Its creation was partly supported by the Open Society Foundations.
[^3]: Platform Cooperativism Consortium, "About", platform.coop.
[^4]: Platform Cooperativism Consortium, "Strengthening the Movement for a Cooperative Digital Economy Through the Platform Co-op Development Kit" (3 September 2018), platform.coop. Made with the Inclusive Design Research Centre at OCAD University.
[^5]: Scholz, T. (2016), *Platform Cooperativism: Challenging the Corporate Sharing Economy*, Rosa Luxemburg Stiftung, New York Office. The ten principles are ownership; decent pay and income security; transparency and data portability; appreciation and acknowledgement; co-determined work; a protective legal framework; portable worker protections and benefits; protection against arbitrary behaviour; rejection of excessive workplace surveillance; and the right to log off.
[^6]: Scholz, T. (2024), *Own This! How Platform Cooperatives Help Workers Build a Democratic Internet*, Verso. Some listings give a December 2023 release.
[^7]: Co-operative News, "Platform co-op movement to hold Solidarity AI conference in Bangkok" (18 March 2026), thenews.coop. The conference is at Chulalongkorn University, 12 to 15 November 2026.
[^8]: Platform Cooperativism Consortium, "News from the Platform Cooperativism Consortium (2025)", platform.coop, on the Istanbul conference, the course AI Without Bosses and the turn towards cooperative AI.
[^9]: Chapter 27 describes the Steward, how releases are adopted, and the sealed code.
[^10]: The guardrails, in short: trust is given by peers, never by yourself and never bought; trust given on doesn't pass on again; trust and money are kept apart, with no way to turn one into the other; money carries no say; value tied to a purpose can't be taken out of it; the Clearing stays off the record; and decisions commit only with enough of the forum behind them and after any concern has been heard; and the floor comes first, an equal amount for every member present, which work never feeds.
[^11]: Chapter 11, Making decisions, on the advice process and consent as the operating system uses them.
[^12]: Chapter 22, The co-pilot, on Wise-Eye: whom it acts for, what it cannot do, how its standing is earned and lost, and what guards against speed and flattery.
[^13]: Chapter 16, The front desk, on callers and cases, what the desk can see, and its rule of saying first that it's an AI.
[^14]: Platform Cooperativism Consortium, "Save the Date: Cooperative AI Conference", platform.coop, on the Istanbul conference of 11 to 14 November 2025, convened with NeedsMap and organised by Trebor Scholz and Stefano Tortorici.
[^15]: Scholz, T., "The Solidarity Stack", talk at the Cooperative AI conference, Istanbul, 2025, platform.coop.
[^16]: Scholz, T., "Reflections on the Cooperative AI Conference" (16 November 2025), platform.coop.
[^17]: Meyer, J., "Can AI Counter Degeneration in Large Cooperatives?" (2 April 2026), platform.coop, written as part of the Institute's fellowship. The study is exploratory, with five cooperatives in Austria and South Tyrol.
