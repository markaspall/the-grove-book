# Measured against Enspiral

<!-- card: The operating system, its networks and The Grove, weighed against Enspiral's own ideas: what we chose, why, and where we might be wrong. -->
<!-- description: Software that promises self-management has a habit of turning a living culture into a set of rules and buttons. Here we set out what we chose for an operating system for organisations and The Grove, the first network of them, how we think it lines up with Enspiral's ideas, and where we might be wrong. -->

*A working draft, November 2026; expect it to change. One of a series weighing what we've built against the work of networks whose ideas we respect.*

---

**In this page**

- What's being measured: an operating system, the networks of organisations running it, and The Grove, the first of them
- Our understanding of Enspiral's ideas, which we'd welcome being corrected on
- Seven of those ideas in turn: what we chose, why, how we think it lines up, and where we might be wrong
- The places we're least sure of, for Enspiral's people to push on

---

If you've spent time around Enspiral, you've probably watched this happen to other people's good ideas. Someone sees a network working without bosses, likes the look of it, and decides the secret must be in the tools. They copy the decision app and the budgeting app, write the agreements into software, and wonder why nothing grows. What made it work was never the software. It was people who knew each other, met in person, looked after each other and kept choosing to stay.

So a reader from Enspiral's world should arrive with suspicions. That this is the tools without the campfire. That rules written into code will be harder to change than a handbook its contributors can edit, and will harden into exactly the structure a do-it-yourself network is trying to avoid. That a system running on clocks will leave no room for the slow relational work that holds a network together. And that code which isn't open sits oddly beside a network that has given away so much of what it learned.

This page doesn't try to argue those suspicions away. It sets out what we chose, why, and how we think it lines up with Enspiral's ideas, so that you can test our reasoning and tell us where it fails.

## What's being measured

Three things, and it helps to keep them apart.

**The operating system** is the software an organisation runs: the rules for seats, decisions, trust, money and work, with a few guardrails at its core that nobody inside an organisation can vote away. It has no name of its own. Each organisation runs its own copy.

**A network** is organisations, each running its own copy of the operating system, that recognise one another and share agreements. It's a network of operating systems, not one system everyone shares. What lets them work together is in the operating system each of them holds, and nobody owns the network. We're building towards each organisation holding its own side of everything it does with others, its services, its needs and its agreements, so that there's no network data held anywhere else. As the code stands, those still sit in one shared store; moving them into each organisation is part of what has to be built before The Grove goes live. Each network has a **Steward**: an organisation that looks after the network's code and ships its releases. The Steward isn't the network, and it holds nothing an organisation needs in order to keep running.

**The Grove** is the first such network. It's still being built and tested. At go-live, each organisation becomes its own independent DAO, running its own copy, and the Steward becomes an organisation in its own right.

One more word used below. Inside an organisation, decisions are made in **forums**. A branch is governed in one forum: the stewards of its parent and of its sibling branches, with the branch's own steward taking part as a person. The root has no parent, so it's governed by its own stewards and the stewards of the branches grown directly from it. Forums are made of people, not branches: someone holding several seats can sit in several forums, and counts once in any one of them. A forum with fewer than two distinct people passes its decisions on towards the root.

We keep to the rule the rest of the book follows: *is* only for what's built, *building towards* for what's decided but not built, and *we don't know* for what's open.

## Our understanding of Enspiral

This is how we understand Enspiral. If we've got any of it wrong, we'd like to be corrected, and we'll change the page.

As we understand it, Enspiral is a network of people and ventures that grew out of Wellington, New Zealand, around Joshua Vial's consulting work. Accounts of when it began differ. Reporting in 2014 put its launch in 2010, when Vial turned his consulting into a collective that found paid contract work for socially minded professionals.[^1] Vial himself has said he registered the name in 2003 as his own consulting brand and turned it into "a collective vehicle" around 2011.[^2] An account by Alanna Krause, one of its early leaders, starts the story in 2008.[^3] We think all three are true of different moments, and we'd welcome the version Enspiral prefers.

Its own handbook describes it as "a network of people who support each other to do meaningful work", while noting that's only one way to put it.[^4] At its centre sits the Enspiral Foundation, a New Zealand limited company with a charitable constitution, owned by shareholders whose shares carry a say and no dividends; it holds the brand and is meant to carry no financial risk.[^5] Around it are ventures, companies started from the network, which relate to the Foundation by agreement and, in one 2016 description, "stand as equals" with no voice weighing more than another.[^6] Loomio, now a worker-owned co-operative, began inside it, when the network gave its first builders a desk.[^2] [^7] For years the network distinguished contributors, invited in by members, from members, who held a share each; in late 2021 Vial described that membership role as being dissolved, and we don't know how far that has gone.[^2] Today it's funded by contributions people choose for themselves,[^8] and as far as we can tell it's still active, with newsletters through 2025, a European gathering near Berlin and a retreat planned by its node near Melbourne. Its annual Summerfest announced a break in 2025, with a smaller gathering in March instead.[^9] We haven't found anything more recent, and if things have moved on, we'd like to know.

From fifteen years of its practice we've drawn seven ideas, the ones we think anyone from Enspiral would reach for when weighing something new:

1. **A network, not a company:** people and ventures around a shared foundation, the campfire rather than the head office.
2. **No bosses, and leadership spread wide:** influence earned, not appointed, with power kept beside responsibility.
3. **Decisions in the open, by consent:** formal decisions on Loomio, where a single block stops most proposals, alongside advice decisions.
4. **Collaborative funding:** a shared pool divided by everyone, bucket by bucket, in Cobudget rounds.
5. **Care as the real infrastructure:** pods, retreats and relationships made in person and kept online.
6. **Contributors invited by members:** belonging that comes by invitation and grows with time.
7. **Open sourcing what you learn:** the handbook, the tools and the stories, given away to be copied and improved.

Enspiral certifies nothing, so this isn't a compliance check. It's our own reading, and it may be a generous one. That's what the sections on where we might be wrong are for.

## 1. A network, not a company

**Our understanding.** Enspiral isn't one company with divisions. It's people and ventures, each running their own affairs, around a foundation that Vial once called "the campfire we all sit around to have a collective discussion".[^1] The Foundation holds the brand and the shared agreements, and is meant not to carry anyone's risk.[^5] Ventures contribute to it and gain from belonging, without being under it.[^6]

**What we chose, and why.** Organisations are where the work is done: each is its own member-run body with its own purpose, money and people. A network is the agreements between them, and the means to make them is in the operating system every organisation holds, so nobody owns it. The Steward keeps the shared code going and ships improvements, and it can't direct any organisation's work. We made the Steward an organisation like any other, bound by the same rules, so that no part of the system sits above the rules the rest live by. Land, money, liability and people stay with each organisation; a network keeps a thin balance sheet, because anything holding everyone's assets becomes a target. The Steward becomes an organisation in its own right from the day The Grove goes live.

**How we think it lines up.** Closely in shape. The organisations are much like Enspiral's ventures, and the network is as thin as Enspiral's foundation tries to be. Where Enspiral's foundation is a campfire, a place people gather, ours is closer to a set of shared rules and a code keeper.

**Where we might be wrong.** Enspiral's centre holds people as well as agreements: shareholders, gatherings, conversation. Our network holds almost nothing, and the Steward looks after code, not relationships. We may have kept the thinness and lost the warmth, and a network with no campfire may find there's nothing to come back to.

## 2. No bosses, and leadership spread wide

**Our understanding.** Enspiral has no management team and no formal authority over anyone; leaders gain influence through the regard of the people around them, and its founder began stepping back from the centre in 2013.[^10] Alanna Irving, one of its co-founders, has described leadership as something that "can and should be distributed among many people and processes", and one of the principles she reaches for is to "align power and responsibility".[^11]

**What we chose, and why.** Nobody in an organisation on The Grove manages anyone. Work belongs to seats, and the people who carry a part of the work decide about it, because they're the ones who live inside the decision on Monday morning (Chapter 10). Influence in a decision is trust, and trust has a narrow meaning: governance weight in one forum, on one kind of matter, given by the peers who sit there. You can't give it to yourself, it can't be passed on again, there's no global score, and money can never buy it (Chapter 12). Each person's choice stands until they change it, and they can change it any day. We've designed trust to fade if it isn't renewed, so that standing never outlives its reasons; that isn't running yet. We chose to write this down because Jo Freeman's warning holds: removing the structure doesn't remove the power, it just hides it (Chapter 12).

**How we think it lines up.** Closely on the principle: power beside responsibility, influence earned from peers, no one above. We differ in method. Enspiral leaves influence to culture; we make it visible and countable inside each forum.

**Where we might be wrong.** Putting a number on influence, even a local one, may change how people treat each other in ways a culture of social capital doesn't. And our own chapter is plain that a centre can grow back by default: a founder whose members hold no seat decides alone (Chapter 10). Enspiral's answer has been a culture in which nobody is in charge. Our design shows the shape but doesn't stop it.

## 3. Decisions in the open, by consent

**Our understanding.** Enspiral's formal decisions are made on Loomio, and its Decisions Agreement says anyone can propose one at any time. A standard proposal runs for at least three working days and passes with no blocks; significant ones, such as changes to the agreements, also need more than half of those taking a position to agree; and "a single block is sufficient to stop a proposal proceeding in most cases". Blocks are meant for a real risk of harm to the network or a clash with its values. An advice decision is made by named people after they've sought input from those affected.[^12] Loomio's own guides frame consent around objections that are reasoned and point to harm rather than preference, and the advice process as anyone deciding after asking those affected and those who know.[^7]

**What we chose, and why.** Consent and the advice process, combined, with a clock in place of the meeting (Chapter 11). Anyone holding a seat in the forum that will hear a change can propose it; any member can raise a tension through the Field. A proposal is checked for shape by someone else in the forum, put out for advice for three to fourteen days to those with skill in what it touches and those it changes, and every member can give advice on any proposal. Then the people seated in the forum consent or raise a concern. A concern has to say what must be answered before they could consent, and holds the proposal until it's met. Silence isn't a concern. A proposal passes when those consenting carry enough of the forum's trust, a fifth, two fifths or two thirds depending on how far the change reaches, and no concern stands. If a concern is still standing ten days from the latest version, the proposal lapses and the tension stays on show, rising through the organisation if nobody answers it. Every change is reviewed, four weeks on by default. We chose clocks because meetings mostly exist to get everyone present at once, and we wanted decisions that move without anyone's evenings.

**How we think it lines up.** Closely: consent rather than majority, objections that name a harm, advice sought widely before deciding. Two differences are deliberate. Enspiral's agreements are changed by everyone in the network together;[^12] ours are decided by the forum that holds the change, with every member asked for advice on the purpose and the agreement. And Enspiral counts each voice the same; we weigh deciders by the trust their peers have given them.

**Where we might be wrong.** A concern still standing after ten days doesn't let the proposal through; the proposal lapses and things stay as they are, which works much like Enspiral's block. The difference is what happens next: the tension stays on show and rises through the organisation, so a lapse can't quietly bury a problem, though a concern can still hold a change back for good. Weighted consent may feel, to someone used to one person and one voice, like the loudest voices getting louder. And the system checks only that a concern has words in it, not that it names a harm, so the line between a reasoned objection and a preference rests on people, as it does at Enspiral, but without the conversation that sits around a Loomio thread.

## 4. Collaborative funding

**Our understanding.** Enspiral's shared money is divided by its people. It began in 2013, when members paid a share of their income into a common pool and a surplus built up; in 2014 Irving and Vial turned that into a spreadsheet and a form, which became the open-source Cobudget.[^13] Today, in a facilitated round, anyone can propose a bucket, the round's money is "divided equally between all participants", and each person places their share where they think it belongs.[^14] Francesca Pick, who has stewarded Cobudget, wrote in 2020 that the network had moved to themed, time-boxed rounds after early ones funded too many small things, and that one round is "like learning Agile and only doing one Sprint".[^13] Cobudget itself has since left Enspiral: Greaterthan, a venture founded by Enspiral people, took it on in 2017, and in 2021 it joined forces with Dreams from the Borderland community, with a Swedish co-operative formed to house the software.[^15] Its code was still being updated in October 2026 and it still takes in contributions, though its last public news is from 2022, so we'd describe it as alive but quiet.[^15]

**What we chose, and why.** Inside an organisation, the books are open to every member. Money never moves through the system; it stays in the organisation's own bank, and the operating system reads its books and governs how the money is allocated. Pay shares a period's earnings by weights the organisation sets for itself, and under it sits a floor, an equal amount for each member, paid first. Income lands in a shared purse, the commons, not with the branch that earned it, and goes to branches by need, through proposals in the root's forum that carry evidence of what the money is for. Money is firewalled from voice: it can fund work but never buy a say. And in the Field, every member's voice weighs the same. What we haven't set out is a way for every member to put a shared pool on the table and divide it between them, bucket by bucket, the way a Cobudget round does.

**How we think it lines up.** Partly. We share the instinct behind the equal split, in the floor and in the Field's one member and one voice, and we share the open books. We have no equivalent of the round itself.

**Where we might be wrong.** A bucket round lets anyone in the network start something and see whether others will back it with money, without asking anyone's permission. That's a kind of initiative our forums, where proposals come from seats, don't offer people without one. We may be underrating how much power shared money gives, and how much belonging comes from deciding together where it goes.

## 5. Care as the real infrastructure

**Our understanding.** Enspiral treats care as work to be shared, not left to chance. Its Pods Agreement sets up groups of four to five people to share "supporting and caring for each other", and says that if you want care in the network, "you have a responsibility to make that happen".[^16] Vial's rule of thumb was to "use in person to establish relationships and use online to maintain them", and the network kept six-monthly gatherings in Wellington from 2011.[^2] Its newsletter in 2025 called retreats "the key rhythm of our network".[^9] Irving is candid that she "burned out multiple times", and the network's book gives real space to looking after each other.[^11]

**What we chose, and why.** Some of the relational life of an organisation has a place in the system and is kept out of its records. The Clearing is a space for being together without an agenda, off the record: nothing said there is kept or read, and nothing feeds any reading. When blame gathers, the response is first release, in the Clearing, and then turning blame into authorship: not "who's at fault?" but "what would you like to see happen?" (Chapter 12). Members appreciate what someone did. Nothing is pushed to anyone: no alert, no phone ringing at three in the morning (Chapter 11). And nothing waits for a meeting, though people can meet whenever they want to.

**How we think it lines up.** Partly, and mostly by restraint. We've tried to keep the system out of the way of care rather than to provide it. We have nothing like pods or retreats, and no part of the operating system brings people together in person.

**Where we might be wrong.** Enspiral's experience suggests the in-person rhythm is what holds everything else up. A system that runs asynchronously, on clocks, may make it easy to belong to an organisation you've never sat down with, and that may be a loss we can't see from inside the software. We've kept relationships off the record to protect them; we may also have left them with no support at all.

## 6. Contributors invited by members

**Our understanding.** For most of its life Enspiral grew by invitation: a member invited someone in as a contributor, and contributors who had been around for a year or so and taken part could become members, holding one share each, which Vial called "your citizenship card in the collective".[^1] Members acted, in his words, as cultural stewards.[^2] That two-step shape is the one he described in 2021 as being dissolved, and we don't know what has replaced it.[^2]

**What we chose, and why.** Joining is a welcome, not a vote (Chapter 10). Someone who holds a seat writes a personal invitation with a note and sends it themselves; whoever opens it reads the organisation's agreement and joins by agreeing to it. The invitation is also a vouch, and it's paced: after an organisation's first thirty days, someone invites only once they've been there two weeks, and no more than two people a week. In a newcomer's first month, if two seat holders other than the inviter question the invitation, the membership is put on hold. Leaving needs nobody's permission and takes effect at once. Belonging and deciding are kept apart on purpose: belonging is a floor that comes by welcome, and deciding follows the work someone carries. A member without a seat can sense in the Field, give advice on any proposal, move work to where it belongs, see the whole, and say they'd like a seat; they can't propose or consent.

**How we think it lines up.** Closely on joining: by invitation, vouched for by someone already inside. We part on what comes next. Enspiral's step was from contributor to member of the whole network; ours is from member to a seat in one part of the organisation, and it's offered by the forum, not reached by time served.

**Where we might be wrong.** Our own chapter says the cost plainly: a member outside every forum has no consent anywhere (Chapter 10). The power to question a newcomer runs one way, from seat holders to members, never back. And if Enspiral decided that the line between contributors and members was worth dissolving, that's evidence we ought to weigh against a design that keeps a line of its own.

## 7. Open sourcing what you learn

**Our understanding.** Enspiral has given away much of what it learned. Its handbook is public and its source is on GitHub, edited by its contributors.[^4] Loomio and Cobudget are open source.[^7] [^15] Its collectively written book, *Better Work Together*, was out by early 2019, and its authors describe it as "blueprints to copy, improve and share".[^17] The habit of writing down its processes and releasing them is one of the things it's best known for.[^3]

**What we chose, and why.** The operating system's code isn't open source. On The Grove, only a few people, seated for the purpose, can read it. We're building towards every organisation carrying the full code with it, sealed, from its first day. The seal opens when organisations that have shown real commitment, verified people holding their root and a record of work done, come together to form a network of their own. Then they can read the code, change it and take it anywhere. We chose this for two reasons. Capture: a system built to stop people being bossed has to be hard to strip of its guardrails and resell under a similar name. And security: every party holding the source is another way in. What an organisation can choose to share with the Steward, and we're building towards this, is its pattern: its general shape and the general kind of work it does, never what any of it says. An organisation whose tension becomes part of a release can be credited for it. And this book itself sets out the reasons behind every choice, in public.

**How we think it lines up.** Partly. The reasoning is open; the code is a bounded commons, shared with those who've shown commitment.

**Where we might be wrong.** Enspiral's tools spread because anyone could pick them up, and Loomio and Cobudget both went on to lives of their own beyond the network, carried by open code. Sealed code asks people to trust guardrails they can't read until they've already committed, and a network that has thrived on giving things away may reasonably see that as the opposite of what it learned.

## Where things stand

| The idea | How we think it lines up |
|---|---|
| A network, not a company | Closely in shape: organisations like ventures, a thin network nobody owns, a Steward that is itself an organisation from go-live. Thinner and cooler than a campfire. |
| No bosses, leadership spread wide | Closely on the principle, different in method: trust given by peers, local to each forum, never bought. One person can keep every decision where seats aren't offered. |
| Decisions by consent | Closely: consent and advice, on clocks, objections that name a harm. A concern still standing after ten days makes the proposal lapse, much as Enspiral's block stops one, and votes are weighted by trust. |
| Collaborative funding | Partly: open books, a shared purse divided by proposal in the root's forum, an equal floor, an equal voice in the Field. Nothing like a bucket round. |
| Care as infrastructure | Partly, by restraint: the Clearing off the record, nothing pushed, no meetings needed. No pods, no retreats. |
| Invitation and belonging | Closely on joining by a vouched invitation. Belonging is a floor; deciding goes with a seat, not with time served. |
| Open sourcing what you learn | Partly: the reasons are public, the code is sealed until committed organisations form a network of their own. |

## Where we're least sure

None of this is Enspiral in software, and we don't claim it is. These are the choices we're least sure of. We'd rather you pushed on our reasoning than took our word for it.

1. **A concern that ends a proposal.** If a concern still stands after ten days, the proposal lapses and things stay as they are. That protects against harm much as Enspiral's block does, but it may let one person hold a needed change back, with only the rising tension to bring it back.
2. **Weighted consent.** We weigh deciders by the trust their peers give them, local to each forum and never bought, so that judgement counts where it's been shown. That may feel like a ranking to people used to one person and one voice, and a number may change a culture that runs on regard.
3. **No shared round.** There is a shared purse, but it's divided by proposals among those seated in the root's forum, not by every member together. Shared money may be one of the strongest ways a network has of belonging, and we haven't designed a way for everyone to divide it.
4. **Care left to people.** We kept the system out of relationships, with the Clearing off the record and nothing pushed. Enspiral's experience says relationships need rhythm and gatherings, and an asynchronous system may make belonging too easy and too thin.
5. **A line between members and seats.** We separated belonging from deciding so that forums stay small and decisions move. Members outside every forum have no consent anywhere, and Enspiral may have found that a line like that is worth dissolving.
6. **Sealed code.** We sealed the code to protect its guardrails from capture. Enspiral's tools went on to lives of their own because their code could go with them, and we may be protecting the code from the very people who would look after it best.

And if we've misread Enspiral's ideas anywhere on this page, please tell us. We'd rather be corrected than be generous to ourselves.

If you'd like to go further, these chapters say more: [Chapter 1, A society of sovereigns](a-society-of-sovereigns.md), on what sovereign means here; [Chapter 10, Belonging without a seat](belonging-without-a-seat.md), on joining, leaving and what a member without a seat can do; [Chapter 11, Making decisions](making-decisions.md), on consent, advice and clocks; [Chapter 12, Trust](trust.md), on trust as governance weight and the Clearing; [Chapter 17, Money and value](money-and-value.md), on the floor and pay; [Chapter 26, Between organisations](between-organisations.md), on services and agreements; and [Chapter 27, DNA, the network, and why not open source](dna-the-network-and-open-source.md), on the sealed code and the Steward.

---

## Notes and further reading

[^1]: Bergren, A. (2014), "Enspiral: Changing the Way Social Entrepreneurs Do Business", *Shareable*, 3 November 2014, shareable.net.
[^2]: "Joshua Vial on Enspiral", *The Jim Rutt Show*, episode 149, 13 December 2021, jimruttshow.blubrry.net.
[^3]: "Enspiral", P2P Foundation Wiki, wiki.p2pfoundation.net, drawing on Alanna Krause's account in the Management Exchange and on the Enspiral FAQ.
[^4]: *The Enspiral Handbook*, handbook.enspiral.com; its source is at github.com/enspiral/handbook.
[^5]: "Enspiral Foundation Ltd", *The Enspiral Handbook*, handbook.enspiral.com/foundation.
[^6]: Cabraal, A. (2016), "Unbundling Enspiral, part 2 of 3: Business", *Enspiral Tales*, Medium, September 2016.
[^7]: Loomio, "About", loomio.com, which describes it as a "worker-owned cooperative" working since 2011; "Loomio", Wikipedia, on its first prototype in 2012 and its roots in the Occupy movement in New Zealand; Loomio, "Consent process" and "Advice process", loomio.com/docs.
[^8]: "Welcome to Enspiral", welcome.enspiral.com, on contributions each person sets for themselves.
[^9]: Enspiral newsletters on Substack, enspiral.substack.com: January 2025 and May 2025, the second on the Enspiral Europe gathering in Stolzenhagen and the Kumara node's retreat near Melbourne. "Summerfest", festival.enspiral.com, on the break in 2025 and a smaller gathering in March.
[^10]: Minnaar, J. (2018), "Meet This Kiwi Bunch Of Organizational Hackers", Corporate Rebels, 15 September 2018, corporate-rebels.com.
[^11]: Sharp, D. (2019), "What Enspiral can teach us about how to run a company with no boss", *Shareable*, 7 May 2019, an interview with Alanna Irving.
[^12]: "Decisions Agreement", *The Enspiral Handbook*, handbook.enspiral.com/agreements/decisions.
[^13]: Pick, F. (2020), "Sharing power by sharing money: the evolution of collaborative funding in Enspiral", *Enspiral Tales*, Medium, March 2020.
[^14]: "Collaborative Funding", *The Enspiral Handbook*, handbook.enspiral.com/money/collabfunding.
[^15]: Pick, F. (2022), "Why Cobudget matters", Greaterthan, Medium, 13 October 2022. Cobudget on GitHub, github.com/cobudget, and on Open Collective, opencollective.com/cobudget.
[^16]: "Pods Agreement", *The Enspiral Handbook*, handbook.enspiral.com/agreements/pods.
[^17]: Cabraal, A., "Better Work Together", *Enspiral Tales*, Medium; and "Book of the Day: Better Work Together", P2P Foundation blog, 2 January 2019.
