# Measured against Sensorica

<!-- card: The operating system, its networks and The Grove, weighed against Sensorica's open value network: what we chose, why, and where we might be wrong. -->
<!-- description: Sensorica has spent fifteen years showing that open peer production can share its rewards by recorded contribution. Here we set out what we chose for an operating system for organisations and The Grove, the first network of them, where we followed the open value network, where we didn't, and where we might be wrong. -->

*A working draft, November 2026; expect it to change. One of a series weighing what we've built against the work of networks whose ideas we respect.*

---

**In this page**

- What's being measured: an operating system, the networks of organisations running it, and The Grove, the first of them
- Our understanding of Sensorica and the open value network, which we'd welcome being corrected on
- Seven of its ideas in turn: what we chose, why, how we think it lines up, and where we might be wrong
- The places we're least sure of, especially on contribution and pay, for the open value network community to push on

---

If you've worked in an open value network, you know why contribution accounting exists. Without a record of who gave what, rewards get settled the old way: by whoever is closest to the money, whoever is most visible, whoever negotiates hardest. The quiet contributor who spent three weekends on the documentation gets thanked and nothing more. A shared, open log of contributions, and a rule agreed in advance for turning it into benefit, was Sensorica's answer to that.

So a reader from this world should arrive with suspicions. That this is a system built around organisations with members, not an open network anyone can step into. That its code is sealed. And, most of all, that it deliberately keeps no log of each person's contributions, and leaves the contribution share of pay to how peers see one another, which sounds like exactly the politics contribution accounting was invented to replace.

This page doesn't try to argue those suspicions away. On contribution in particular, we've chosen differently from Sensorica, and we may be wrong. It sets out what we chose, why, and how we think it lines up with Sensorica's ideas, so that you can test our reasoning and tell us where it fails.

## What's being measured

Three things, and it helps to keep them apart.

**The operating system** is the software an organisation runs: the rules for seats, decisions, trust, money and work, with a few guardrails at its core that nobody inside an organisation can vote away. It has no name of its own. Each organisation runs its own copy.

**A network** is organisations, each running its own copy of the operating system, that recognise one another and share agreements. It's a network of operating systems, not one system everyone shares. What lets them work together is in the operating system each of them holds, and nobody owns the network. We're building towards each organisation holding its own side of everything it does with others, its services, its needs and its agreements, so that there's no network data held anywhere else. As the code stands, those still sit in one shared store; moving them into each organisation is part of what has to be built before The Grove goes live. Each network has a **Steward**: an organisation that looks after the network's code and ships its releases. The Steward isn't the network, and it holds nothing an organisation needs in order to keep running.

**The Grove** is the first such network. It's still being built and tested. At go-live, each organisation becomes its own independent DAO, running its own copy, and the Steward becomes an organisation in its own right.

One more word used below. Inside an organisation, decisions are made in **forums**. A branch is governed in one forum: the stewards of its parent and of its sibling branches, with the branch's own steward taking part as a person. The root has no parent, so it's governed by its own stewards and the stewards of the branches grown directly from it. Forums are made of people, not branches: someone holding several seats can sit in several forums, and counts once in any one of them. A forum with fewer than two distinct people passes its decisions on towards the root.

We keep to the rule the rest of the book follows: *is* only for what's built, *building towards* for what's decided but not built, and *we don't know* for what's open.

## Our understanding of Sensorica

This is how we understand Sensorica. If we've got any of it wrong, we'd like to be corrected, and we'll change the page.

As we understand it, Sensorica is an open value network based in Montreal, which went online on 11 February 2011 and describes itself as "an OVN, not a traditional organization."[^1] It was founded by Tiberius Brastaviceanu, Ivan Pavlov and François Bergeron.[^2] Its work is open hardware: sensors and sensemaking instruments, and more recently medical and fabrication ventures, built by affiliates who combine paid work with work done for its own sake.[^3] It isn't a company, a co-operative or a charity. It describes itself legally as a non-registered association, and it holds assets and meets the market through separate bodies, a custodian and one or more exchange firms.[^4] One interview gives 2010 as the year it was created, so the founding date depends on what's counted.[^3]

Sensorica coined the term "open value network" and, around 2012, built the Network Resource Planning software, NRP, with Bob Haugen and Lynn Foster, to log contributions and share benefits. That work fed the Valueflows vocabulary for economic networks, begun in 2014, which grew from the Resource, Event, Agent model of accounting.[^5] Its newer work, Nondominium, is a Holochain application for sharing resources that no one party controls; Sensorica lists it as at the prototyping and funding stage, with at least one funding proposal unsuccessful.[^6]

On its current state we're less certain. Its blog is active through 2026, with posts on Nondominium, open medical devices and an educational programme in collaborative entrepreneurship.[^7] Some of its own terms have changed: what it once called the "value equation" it now calls the "benefit redistribution algorithm", and "value accounting" has become "contribution accounting".[^8] And its model is argued over. A 2024 paper by Nancy Ettlinger questioned whether its reputation systems become a kind of social control and whether it scales; in April 2026 Sensorica published a point by point reply disagreeing with much of it.[^9] We haven't read every side of that exchange, and we'd welcome being told what we've missed.

Over fifteen years Sensorica has produced ideas that anyone from this world will reach for when weighing something new. We've used seven:

1. **The open value network:** an open, decentralised, self-organising network where people create value together and share the income, rather than an organisation with a wall around it.
2. **Open access:** permissionless participation, in the work and in planning and decision-making.
3. **Contribution accounting:** an open record of every affiliate's contributions of time, money and materials, evaluated in context.
4. **Benefit redistribution:** an algorithm, agreed before the work begins, that turns recorded contributions into a share of what a venture earns.
5. **Reputation and roles:** reputation that guides people to suitable work and shapes benefit, and roles taken up by voluntary subordination.
6. **Custodianship and nondominium:** shared assets held in trust by a custodian, under a regime where no participant has a dominant right over them.
7. **Ventures in a network:** many self-governed ventures sharing one environment, contributing to its infrastructure and free to fork and remix.

Sensorica certifies nothing, so this isn't a compliance check. It's our own reading, and it may be a generous one. That's what the sections on where we might be wrong are for.

## 1. The open value network

**Our understanding.** An open value network is a way for people to create value together, contributing work, money and goods, and to share the income that results. Sensorica calls itself "an open, decentralized, and self-organizing value network", combining a market economy with a gift economy, and coordinating largely by stigmergy: people see what needs doing in a shared environment and take it up.[^3] It avoids formal membership categories with special privileges.[^3]

**What we chose, and why.** We chose the organisation as the unit, not the open network. Each organisation is its own member-run body with its own purpose, money and people, and a network is the agreements between organisations, each running its own copy of the operating system. Inside an organisation, work isn't organised around jobs: it's organised in branches, each shaped around a piece of work, never a person, and the shape keeps changing by proposal as the work changes. We chose a boundary because the things an organisation answers for, its promises, its money, its liability, the people who depend on it, need someone who answers for them, and we couldn't see how to give that a clear home in a network open to everyone.

**How we think it lines up.** A different shape, chosen deliberately. What we share is the refusal of a boss and the wish for structure to follow the work. Where Sensorica is open first and builds structure as ventures need it, we start from a bounded organisation and open it outwards.

**Where we might be wrong.** A boundary is a cost to exactly the kind of contribution an open value network lives on: the person who sees something worth doing and does it, without being asked or admitted first. A system built around organisations may harden into the organisational forms Sensorica set out to move past. And our answer to "who answers for it" may be one an open network has already solved in another way, through its custodian and exchange firms, without needing a wall.

## 2. Open access

**Our understanding.** By open, Sensorica means "permissionless access to participation", and access to planning and decision-making too.[^4] Its ventures say "anyone can join".[^1]

**What we chose, and why.** Joining an organisation is by personal invitation, and agreeing to the organisation's agreement. Members can sense, give advice, move work to where it belongs and see the whole; only those holding a seat can propose and decide. People outside the membership take part when invited into a sensing, answering by link, their voice kept beside the members' rather than mixed into it. Anyone can become active with an organisation, a customer, a supplier, a neighbour, and hold a seat, as far as the organisation's needs allow. We're building towards identity checks that step up with governance responsibility rather than with wealth: the more say someone carries, the more the organisation needs to know they're real. We chose this because an invitation is also a vouch: it guards against people being brought in by the dozen to swing things, and until identity checks run, it's what stands behind a seat holder.

**How we think it lines up.** Not closely. Ours is open by invitation, and the door to a seat opens as far as an organisation needs. Theirs is open by default.

**Where we might be wrong.** Invitation runs along the lines of who already knows whom, and that's one of the oldest ways power hides. We named that risk ourselves, citing Jo Freeman, in Chapter 12.[^10] An organisation that grows only by invitation may end up looking like its founders. And permissionless participation may be safer than it looks, if what's open is the work and what's guarded is the money, which is roughly how Sensorica's custodian arrangement reads to us.

## 3. Contribution accounting

**Our understanding.** Tiberius Brastaviceanu's case is that peer production needs a system that can "record everyone's contribution, evaluate these contributions, and calculate every participant's fair share", and that this is "not a currency, not a barter system."[^11] Sensorica's NRP contribution accounting system logs contributions of time, money and materials against the resources they built, with space and social capital still to come.[^3] Its point, as we read it, is that a shared open record protects the contributor whose work would otherwise go unseen.

**What we chose, and why.** This is where we differ most, and we want to set it out carefully.

- **No contribution log.** The operating system keeps no log that tallies what each person gave, and no points, scores or counts about people. What someone did stays in the record of the work, but the read, the continuous reading of what work does in each branch, has no place for a person. Reputation is never published, and each person sees only their own. We chose this because a number attached to a person becomes something to rank, fear or game, and because an organisation reading its own work should read the work, not the people.
- **Open books, for money.** What is open is the money. Every member can read the books, every loan and what's free to spend, and money recorded on someone's word is open to question for a week.
- **What pay rests on instead.** Pay shares a period's earnings by weights the organisation sets for itself: hours given, seats held, contribution as the organisation's own peers see it, and equal shares. Out of the box the contribution weight is off and everything is shared by hours given. When an organisation turns it up, it follows recognition from peers and how the work turned out, never a ranking of people.[^12] Revenue booked to a branch is never a basis for pay, so the people who care, sense and hold the work aren't starved by those whose work happens to show up as income.
- **A fuller view, not built.** We've designed a way to look through three channels at once, the trust peers have given, what the work itself shows someone doing, and colleagues confirming that someone shows up, so that a gap between them prompts a second look: steady work with little trust, say, which may be a quieter person worth noticing. We haven't built it, and when we do, it has to keep the rule that no reading ever scores a person.[^10]

**How we think it lines up.** Partly. We share the aim: that the mentor, the carer and the quiet builder are paid something real, and that revenue isn't the measure of value. On the means, we've taken the other road. Sensorica records contributions and shares by the record; we record money openly and leave contribution to how peers see it, if an organisation chooses to weigh it at all.

**Where we might be wrong.** This is the choice we're least sure of. Peer recognition is open to exactly the bias contribution accounting guards against: people tend to recognise whoever is most visible, and a log of the three weekends on the documentation doesn't depend on anyone noticing them. Hours given rewards time spent rather than what came of it. Contribution as peers see it becomes something worth gaming once it carries any share of pay, and it may be easier to game than a record anyone can check. Sensorica's own reply to its critics was that benefits follow "results, not badges".[^9] We may have avoided scoring people at the price of making their contribution harder to see, which is the very thing our three channels were meant to fix and haven't yet.

## 4. Benefit redistribution

**Our understanding.** The benefit redistribution algorithm, first proposed in 2011 as the value equation, turns recorded contributions into each contributor's share of a venture's revenue. It weighs kinds of contribution, time, money and so on, against things like frequency, quality and the priority of the task. Each venture can have its own, with one version for ventures that sell, looking back at past contributions, and another for ventures funded by grants or donations, looking forward against a plan.[^13] It's set at the start: Tiberius Brastaviceanu calls it "a contract among participants",[^11] and "a social contract among affiliates", with its weights "agreed upon democratically."[^14] What participants earn is a claim on future revenue, for the product's lifetime, with the risk shared among them.[^15]

**What we chose, and why.** An organisation sets one allocation, by a proposal in the forum around its root: how much of each period's profit is kept for growth, how big the floor is, and how the rest is shared between hours given, seats held, contribution and equal shares. The seats part follows the seat, not the person. Until that proposal is agreed, nothing is paid. Under all of it sits a floor, an equal amount for each member, paid first. As built, the floor comes from each period's profit, so a lean month can leave it empty; we're changing it to come from what the organisation has free, capped so it can never pay out more than is there. We're building towards a share of the upside for those who built it, and towards a taper for people who automate their own role, so that teaching the AI to do your work doesn't cost you your share overnight.[^12] We chose one set of weights for the whole organisation, rather than a scheme per project, so that organisations with very different temperaments could use the same machinery and their choices would be visible.

**How we think it lines up.** In spirit, closely: a rule for sharing, agreed by those it binds, before the money arrives. In mechanism, differently. Theirs follows each contribution into the revenue of the venture it built. Ours shares an organisation's profit, period by period, by weights its forum sets and can change.

**Where we might be wrong.** Sharing each period's profit doesn't follow risk. Someone who gave a year before there was any revenue may get nothing for it, and the share of upside that would answer that isn't built. A venture's own equation can fit the work it rewards; one set of weights for a whole organisation may fit none of its parts well. And because the allocation can be changed by a later proposal, it's less of a contract than Sensorica's: people can't count on what they were promised when they began.

## 5. Reputation and roles

**Our understanding.** In Sensorica, reputation helps direct people to suitable tasks and encourages good conduct, and in its earlier accounting higher formal reputation gave higher equity, all else being equal.[^3] [^15] Roles guide self-organisation through "voluntary subordination": people choose to take up a role and the responsibilities that go with it, sometimes with financial incentives attached.[^3]

**What we chose, and why.** We split what Sensorica keeps together. **Trust** is governance weight: how much say someone carries in a particular forum, on a particular kind of matter, given by peers, never by yourself, never passed on, never bought. Someone who sits in ten forums has ten small, separate standings, never one big one. We designed trust to fade if it isn't renewed; that isn't running yet. **Reputation** is a wider picture of skill in each kind of matter, built from peers' commendations and how proposals actually landed. It decides who is asked for advice and never enters the decision itself, and it's never published. **Trust and money are kept apart**, with no way to turn one into the other. **Seats** are our nearest thing to roles: a branch has one seat, it can be shared, nobody takes one by their own proposal unless they'd decide alone anyway, and anyone can step down.[^10] We chose to keep reputation private and out of both decisions and money because a global reputation is a single target for capture, and because nobody is equally good at everything.

**How we think it lines up.** On roles, closely: taking up a seat is close to voluntary subordination, and a seat, like a role, belongs to the work, not the person. On reputation, differently: in Sensorica it's a shared signal that can shape benefit; in ours it's a private mirror that only shapes who is asked for advice.

**Where we might be wrong.** A reputation nobody else can see can't be questioned either, and invisible standing is exactly the danger we wrote about in Chapter 12. Sensorica's reply to its critics was that the fear of reputation as a means of social control is overstated;[^9] if that's right, our privacy may cost an organisation useful knowledge about who is good at what. And without trust fading, which isn't running, standing in a forum can settle in much the way it does in the organisations we set out to replace.

## 6. Custodianship and nondominium

**Our understanding.** Sensorica distinguishes commons, for shared resources that need little looking after, such as digital designs, from nondominium, for assets that can't simply be owned in common: a form of property in which no participant has a dominant right over a resource, an idea first proposed by Chris Cook.[^16] Members pass their rights to a custodian, a body set up as a trust, which gives back a set of rights under a custodian agreement; those rights can't be divided or traded, the agreement changes only by unanimous consent, and on dissolution the assets are given away rather than shared out.[^16] Its Montreal lab is held this way.[^16] Custodians have changed over time: one served until 2020 and is now inactive, and a different one holds the PEP Master venture.[^3] [^4]

**What we chose, and why.** We put the lock inside the organisation rather than in a separate custodian. Value tied to an organisation's purpose can never be taken out of it, not even by everyone agreeing: a locked asset is never sold, given away or written off, it can move between branches, still locked, and there's no unlock. Anyone who depends on something the organisation holds, as a home, a livelihood, a supply or a way in, goes on record, and a proposal to part with it can't be made until it carries a landing for each of them. That's built. The operating system never holds or moves an organisation's money; the money stays in the organisation's own bank, and the operating system keeps the books beside it.[^12] We're building towards an optional legal form, owned by the organisation's members, that carries its decisions into the legal world, with a purpose lock beside it. Between organisations, a network keeps a thin balance sheet: agreements and shared code, not land. For networks of physical sites we've sketched borrowing the Mietshäuser Syndikat's lock against selling a site off. That's a sketch, not something we've built.

**How we think it lines up.** Closely in intent: what's held for a purpose can't be captured by any one party, the members included. Differently in where the lock sits. Sensorica's sits with a trust outside the venture; ours sits in the organisation's own rules.

**Where we might be wrong.** A lock in software is only as strong as the law it meets. Until the legal form is built, a court, a bank or a creditor may see the organisation's assets as belonging to whoever's name is on the account, and a custodian in law may be the stronger safeguard. A lock inside one organisation also does nothing for an asset that several organisations build and use together, which is exactly the case nondominium was made for, and our thin network has nowhere to hold it.

## 7. Ventures in a network

**Our understanding.** Sensorica is many ventures in one environment. Each is self-governed within the network's governance, has at least one custodian and can have exchange firms, can have sub-ventures, and can be forked or remixed. Ventures with tangible benefits give five per cent towards the upkeep of the network's shared infrastructure, and resources created in the environment are shared among all ventures.[^17] The Valueflows lineage carries the same thought between networks: a shared vocabulary so that independent organisations can coordinate their economic flows.[^5] [^8]

**What we chose, and why.** Inside an organisation, branches are something like ventures: each holds its own purpose and work, can grow smaller branches, and changes shape by proposal as the work changes. Between organisations, a branch can offer a service at its own price, post a need, and make an agreement with another organisation by a proposal on each side, looked back on every ninety days by default. When one organisation provides a service to another, what it earns is its own; the Steward takes nothing from what passes between organisations. An organisation's DNA, its purpose, documents, playbooks and people, stays its own and goes with it if it divides. The shared code is funded differently from Sensorica's infrastructure: the Steward charges for its own services, setting organisations up, its starter packs and the plan an organisation pays for, with a margin on top. That margin pays for maintaining the code and its testing, the models the operating system uses, hardware, running costs and making the idea known. How large it should be is open.

**How we think it lines up.** Partly. Self-governing parts, free to divide, inside a larger whole, is close to Sensorica's ventures. The funding of what's shared is not: theirs is a contribution set by the network, ours is a margin set by the Steward.

**Where we might be wrong.** A margin is a risk, and we'd rather name it than hide it. A guard that's paid can grow fond of being paid, and while there's one network there's one Steward, so the cost of leaving does less to keep the price honest than it will when there are others. A share given by every venture to the infrastructure all of them use, as Sensorica does, may be the fairer arrangement. And networks may need to speak a shared vocabulary such as Valueflows if organisations in different networks are to see each other's services and agreements. Whether ours should, we don't know yet.

## Where things stand

| The idea | How we think it lines up |
|---|---|
| The open value network | A different shape, by choice: bounded organisations opening outwards, not an open network building structure inwards. |
| Open access | Not closely: membership by invitation, guests by link, a seat as far as an organisation's needs allow. |
| Contribution accounting | Partly: open books for money, but no log of each person's contributions, and no points, scores or counts about people. |
| Benefit redistribution | Close in spirit, different in mechanism: one set of weights per organisation, a floor paid first, contribution an optional weight as peers see it. A share of the upside is building towards. |
| Reputation and roles | Seats close to roles. Reputation private and kept out of decisions; trust kept apart from money. |
| Custodianship and nondominium | Close in intent: purpose lock and landings are built. The legal form is building towards; nothing held across organisations. |
| Ventures in a network | Partly: branches and organisations divide freely; shared code funded by the Steward's margin, whose size is open. |

## Where we're least sure

Sensorica has lived with its model for fifteen years and we've lived with ours on a test bench. These are the choices we're least sure of, and we'd rather you pushed on our reasoning than took our word for it.

1. **No log of each person's contribution.** We chose it so nobody becomes a number. It may leave the quiet contributor less visible than a contribution log would, which is the harm both of us set out to prevent.
2. **Contribution as peers see it.** It's one optional weight, off by default. Once it carries pay it's worth gaming, and recognition tends to follow visibility rather than work.
3. **Pay that doesn't follow risk.** Sharing each period's profit is simple and changeable. It doesn't reward those who gave before there was revenue, and the upside share that would isn't built.
4. **A private reputation.** We kept it to a mirror so it can't be captured or turned into a ranking. A standing nobody can see is also one nobody can question.
5. **Membership by invitation.** We chose it as a vouch, against people being brought in to swing things. It runs along existing networks and may close the door on the contributor Sensorica was built for.
6. **A lock inside the organisation, and a Steward's margin outside it.** The lock may not hold in law until the legal form exists, and a margin set by the Steward may be a weaker answer than a share set by the network.

And if we've misread Sensorica's ideas anywhere on this page, please tell us. We'd rather be corrected than be generous to ourselves.

If you'd like to go further, these chapters say more: [Chapter 9, The branch: cells, not jobs](the-branch.md), on branches and seats; [Chapter 10, Belonging without a seat](belonging-without-a-seat.md), on members, guests and joining; [Chapter 12, Trust](trust.md), on trust, reputation and why there's no global score; [Chapter 17, Money and value](money-and-value.md), on the commons, the floor and pay; [Chapter 26, Between organisations](between-organisations.md), on services and agreements; [Chapter 27, DNA, the network, and why not open source](dna-the-network-and-open-source.md), on the sealed code and the Steward; and [Chapter 28, Growing a sustainable network](growing-a-sustainable-network.md), the strawman for physical sites.

---

## Notes and further reading

[^1]: Sensorica, home page, sites.google.com/view/sensorica/home: "an OVN, not a traditional organization"; online since 11 February 2011; "All ventures are open and collaborative, anyone can join!"
[^2]: "Sensorica", Wikipedia, on its founding in February 2011 by Tiberius Brastaviceanu, Ivan Pavlov and François Bergeron.
[^3]: "Sensorica", P2P Foundation Wiki: "an open, decentralized, and self-organizing value network"; its custodian and exchange firm; the contribution accounting system and what it logs; reputation; roles and "voluntary subordination"; an interview giving 2010 as the year it was created.
[^4]: Sensorica, "Q and A", sites.google.com/view/sensorica/help/qanda: "permissionless access to participation"; a non-registered association under the Civil Code of Québec; custodians past and present.
[^5]: Open Cooperative Ecosystem, "History", oce.gitbook.io, on Sensorica coining "open value network" and building NRP with Bob Haugen and Lynn Foster in 2012, and Valueflows beginning in 2014. Haugen, B. (2024), "Valueflows overview", write.as/economic-networks, on Valueflows as "a vocabulary for the distributed economic networks of the next economy", built on the Resource, Event, Agent model first published by William McCarthy in 1982.
[^6]: Sensorica, "Nondominium", sites.google.com/view/sensorica/ventures/infrastructure/nondominium, on its Holochain basis, its use of Valueflows, and its status as "Prototyping and funding stage".
[^7]: Sensorica blog, sensoricablog.blogspot.com, posts from March to August 2026.
[^8]: The renamings are noted in "Benefit Redistribution Algorithm", P2P Foundation Wiki, and in note 9.
[^9]: Sensorica blog (22 April 2026), "Our feedback on: Cautious hope: Prospects and perils of communitarian governance in a Web3 environment", responding to Ettlinger, N. (2024), "Cautious hope: Prospects and perils of communitarian governance in a Web3 environment". We've read Sensorica's reply, not the paper itself.
[^10]: Chapter 12, Trust, and Chapter 10, Belonging without a seat. Freeman, J. (1972), "The Tyranny of Structurelessness".
[^11]: Brastaviceanu, T., "Why do we need a contribution accounting system?", P2P Foundation blog, first published 3 January 2014, last modified 8 January 2018.
[^12]: Chapter 17, Money and value.
[^13]: "Benefit Redistribution Algorithm", P2P Foundation Wiki.
[^14]: "Tiberius Brastavicenau on the Open Value Networks Practice at Sensorica", P2P Foundation Wiki.
[^15]: "Value Accounting System", P2P Foundation Wiki.
[^16]: "Nondominium", P2P Foundation Wiki, on Chris Cook's concept, Kurt Laitner's framework for Sensorica, the custodian agreement and the Montreal lab.
[^17]: Sensorica, "Help for ventures", sites.google.com/view/sensorica/help/venture-help.
