# Measured against the P2P Foundation

<!-- card: The operating system, its networks and The Grove, weighed against the P2P Foundation's own ideas: what we chose, why, and where we might be wrong. -->
<!-- description: Platforms that speak the language of peers have a habit of selling the shared work back to the people who made it. Here we set out what we chose for an operating system for organisations and The Grove, the first network of them, how we think it lines up with the P2P Foundation's ideas, and where we might be wrong. -->

*A working draft, November 2026; expect it to change. One of a series weighing what we've built against the work of networks whose ideas we respect.*

---

**In this page**

- What's being measured: an operating system, the networks of organisations running it, and The Grove, the first of them
- Our understanding of the P2P Foundation's ideas, which we'd welcome being corrected on
- Seven of those ideas in turn: what we chose, why, how we think it lines up, and where we might be wrong
- The places we're least sure of, for the commons movement to push on

---

If you've followed the commons movement for any length of time, you've seen this before. Someone builds a platform for collaboration. It speaks the language of peers, self-management and shared value. The early users do the real work: they bring their organisations, their patterns, their trust. Then whoever owns the platform turns that shared work into a product and sells it back, and the users find they've built someone else's asset.

So a reader from the commons world should arrive with suspicions. That this is a platform with a friendly face, and someone owns it. That its code isn't open, which in this world usually means it isn't really a commons. That it runs on a blockchain, and blockchains have a long record of turning cooperation into speculation.

This page doesn't try to argue those suspicions away. It sets out what we chose, why, and how we think it lines up with the P2P Foundation's ideas, so that you can test our reasoning and tell us where it fails.

## What's being measured

Three things, and it helps to keep them apart.

**The operating system** is the software an organisation runs: the rules for seats, decisions, trust, money and work, with a few guardrails at its core that nobody inside an organisation can vote away. It has no name of its own. Each organisation runs its own copy.

**A network** is organisations, each running its own copy of the operating system, that recognise one another and share agreements. It's a network of operating systems, not one system everyone shares. What lets them work together is in the operating system each of them holds, and nobody owns the network. We're building towards each organisation holding its own side of everything it does with others, its services, its needs and its agreements, so that there's no network data held anywhere else. As the code stands, those still sit in one shared store; moving them into each organisation is part of what has to be built before The Grove goes live. Each network has a **Steward**: an organisation that looks after the network's code and ships its releases. The Steward isn't the network, and it holds nothing an organisation needs in order to keep running.

**The Grove** is the first such network. It's still being built and tested. At go-live, each organisation becomes its own independent DAO, running its own copy, and the Steward becomes an organisation in its own right.

One more word used below. Inside an organisation, decisions are made in **forums**. A branch is governed in one forum: the stewards of its parent and of its sibling branches, with the branch's own steward taking part as a person. The root has no parent, so it's governed by its own stewards and the stewards of the branches grown directly from it. Forums are made of people, not branches: someone holding several seats can sit in several forums, and counts once in any one of them. A forum with fewer than two distinct people passes its decisions on towards the root.

We keep to the rule the rest of the book follows: *is* only for what's built, *building towards* for what's decided but not built, and *we don't know* for what's open.

## Our understanding of the P2P Foundation

This is how we understand the Foundation. If we've got any of it wrong, we'd like to be corrected, and we'll change the page.

As we understand it, the P2P Foundation is a non-profit research body and global network, registered in the Netherlands and active since 2005, that studies and promotes commons-oriented peer-to-peer dynamics in society, and works to help people, organisations and governments move towards commons-based approaches.[^1] Its wiki is one of the largest collections of knowledge about peer production anywhere. It documents projects rather than building them, and describes itself as an organised network that helps networks form without directing them.[^2]

Over two decades its research has produced ideas that anyone from this world will reach for when weighing something new. We've used seven:

1. **The three institutions of peer production:** a productive community, an entrepreneurial coalition and a for-benefit association.
2. **Generative, not extractive:** value made in common shouldn't be captured by whoever owns the platform it runs on.
3. **Open cooperativism:** cooperatives oriented to the common good, governed by their stakeholders, co-producing commons, and organised globally.
4. **Reciprocity licensing:** knowledge free to those who contribute to it, with reciprocity asked of those who only profit from it.
5. **Open books and contributory accounting:** value recognised beyond the price signal, with the books open to those who take part.
6. **Cosmo-localism:** what's heavy stays local, what's light is global and shared.
7. **Commons infrastructure:** the tools a commons runs on should be held in common too, not rented.

The Foundation certifies nothing, so this isn't a compliance check. It's our own reading, and it may be a generous one. That's what the sections on where we might be wrong are for.

## 1. The three institutions of peer production

**Our understanding.** Peer production tends to settle into three kinds of institution: a productive community that builds a shared resource, an entrepreneurial coalition that makes livelihoods on top of it, and a for-benefit association that keeps the infrastructure of cooperation alive without directing the work.[^3]

**What we chose, and why.** Organisations are where livelihoods are made: each is its own member-run body with its own purpose, money and people. A network is the agreements between them, and the means to make them is in the operating system every organisation holds, so nobody owns it. The Steward keeps the shared code going and ships improvements, and it can't direct any organisation's work. We made the Steward an organisation like any other, bound by the same rules, rather than a separate kind of body, because we didn't want any part of the system to sit above the rules the rest live by. The Steward becomes an organisation in its own right from the day The Grove goes live.

**How we think it lines up.** Closely: organisations as the coalition, the Steward as the for-benefit role. The productive community is less clear-cut. Inside each organisation it's the members; across a network, it's whoever contributes back to the shared code and patterns.

**Where we might be wrong.** A foundation's charter can be harder to change than an organisation's rules, so a Steward governed like everyone else might be a weaker safeguard, not a stronger one. And a Steward with seats of its own might, over time, start to direct what it was meant only to support.

## 2. Generative, not extractive

**Our understanding.** The Foundation's name for the pattern at the top of this page is netarchical capitalism: value made by a commons and captured by whoever owns the network it runs on.[^4] The generative alternative keeps the value with those who create it.

**What we chose, and why.**

- **What an organisation holds.** We're building towards each organisation being its own unit of software on the Internet Computer, holding its own records, documents and decisions, and controlled by its own decision-making from the day it's created. Nobody will be able to push code into an organisation: adopting a release will be its own decision, by its own proposal, with a delay and a way back. We chose this so that there's nothing for an owner of the network to capture, because the network holds nothing an organisation needs.[^5]
- **What leaves an organisation.** An organisation can choose to share its pattern with the Steward, and it's less than it sounds. No text leaves: not its purpose, accountabilities, practices or measures, and nothing anyone has written. The pattern is made inside the organisation's own core, and it carries only the general shape of the organisation and the general kind of work it does, not what any of it says. Its DNA, the living whole of its purpose, documents, playbooks and people, never leaves. An organisation that shares gets back what's working for organisations like it; one that doesn't loses only that. We're building towards this.
- **Who earns.** When one organisation provides a service to another, what it earns is its own; the Steward takes nothing from what passes between organisations. The Steward charges for its own services, setting organisations up, its own starter packs and the plan an organisation pays for, with a margin on top. That margin pays real costs: maintaining the code, the AI agents that help write it, testing it for how it looks and feels to use, how it holds up at scale and how it stands up to attack, much of which spends AI tokens too, hardware and computing, training and testing the models the operating system uses, its own running costs on the chain, and making the idea known. How large the margin should be is open.

Without a margin there would be no Steward. The code would have to be open to everyone, and then the questions become who can see it, who maintains it, and who stops someone stripping out its guardrails and selling it on. The Steward is a guard as much as a maintainer. We'd rather name the margin as a risk than pretend it isn't there. Any organisation can offer starter packs and services to others, at any price, including free. And what a Steward can charge is held in check by the cost of leaving: organisations can detach and run alone, or, once they've shown real commitment, form a network with a Steward of their own.
- **Who can't buy a say.** Trust and money are kept apart, with no way to turn one into the other, so money can fund the work but never buy a voice. That's one of the guardrails in the operating system's core, which no organisation can vote away, not even unanimously.[^6]

**How we think it lines up.** Well, by design. The value an organisation creates stays in it, and the Steward earns from its own work, not from a cut of everyone else's.

**Where we might be wrong.** A margin is a risk. The commons world has good reasons to be wary of a for-benefit role that earns one, and a guard that's paid can grow fond of being paid. The cost of leaving only disciplines price if there's somewhere to go, and while there's one network, there's one Steward. And a Steward that sees many organisations' shared patterns may be gathering a kind of value that ought to belong to the network rather than to it.

## 3. Open cooperativism

**Our understanding.** Open cooperativism asks a cooperative fit for the age of networks to do four things: be oriented by its own rules towards the common good; be governed by all its stakeholders; co-produce commons, immaterial and material; and organise globally while producing locally.[^7]

**What we chose, and why.**

- **Oriented to the common good.** Value tied to an organisation's purpose can never be taken out of it, not even by everyone agreeing. Trust is given by peers and can never be bought. These rules are written into the operating system's core and checked by tests. We've also designed trust to fade if it isn't renewed, so that power never settles; that isn't running yet. We chose rules in the core over rules in a document because documents get amended when people are tired.
- **Governed by those who carry the work, and heard by those it touches.** We gave nobody a seat by category. Stakeholders aren't seated as a group; their part is passive by default. But anyone can become active with an organisation: a customer, a supplier, a neighbour can join it and hold a seat, as far as the organisation's needs allow. The operating system uses the advice process: any member can give advice on any proposal; it's actively asked of those the change affects and those with proven skill in what it touches; and the people seated in the forum decide by consent, meaning nobody there holds a reasoned objection.[^8] We chose this because seats by category tend to turn decisions into negotiations between interests, and we wanted decisions made by the people closest to the work, with everyone affected heard first and anyone free to come closer.
- **Where being affected gives more than a voice.** Anyone who depends on something the organisation holds, as a home, a livelihood, a supply or a way in, goes on record. A proposal to part with it can't be made until it carries a landing for each of them, and where the thing is locked to the purpose, those who depend on it can stop it being moved.[^9] That's built.
- **People outside the membership** take part when invited into a sensing, answering by link, their voice kept beside the members' rather than mixed into it.

**How we think it lines up.** Strongly on the common good. On co-producing commons, partly; see reciprocity below. On organising globally, yes; see cosmo-localism. On stakeholder governance we've taken a different road, deliberately.

**Where we might be wrong.** Being heard isn't the same as having a share in the decision. The door to a seat is open, but it opens only as far as an organisation needs, and the people most affected by an organisation, customers, neighbours, suppliers, may need more than that. Our choice may protect the people inside at the expense of the people around them.

## 4. Reciprocity and a bounded commons

**Our understanding.** Commons-based reciprocity licences, copyfair and the Peer Production License among them, keep knowledge free to those who contribute to the commons and ask for reciprocity from those who only profit from it.[^10]

**What we chose, and why.** The operating system's code isn't open source. On The Grove, only a few people, seated for the purpose, can read it. We're building towards every organisation carrying the full code with it, sealed, from its first day. The seal opens when organisations that have shown real commitment, verified people holding their root and a record of work done, come together to form a network of their own. Then they can read the code, change it and take it anywhere.

We chose this for two reasons. Capture: a system built to stop people being bossed has to be hard to strip of its guardrails and resell under a similar name, and an open kernel can be taken by anyone well funded. And security: every party holding the source is another way in. We chose to carry the sealed code with every organisation from the start, rather than release it on leaving, so that a captured Steward could never hold it back.

Value flows back in three ways. An organisation whose tension becomes part of a release can be credited for it; organisations are credited, never people. A network that offers an improvement back gets it back as functionality, along with everyone else, and no money changes hands. And an organisation's DNA stays its own, going with it if it divides. The licence for code once the seal opens is still open, with legal advice to come, and copyfair is one of the options.

**How we think it lines up.** Partly. It's a bounded commons: shared with those who've shown commitment, not with everyone.

**Where we might be wrong.** A commons shared only with the committed may not be a commons at all, and sealed code asks people to trust guardrails they can't read until they've already committed. A reciprocity licence might protect against capture as well as earned access does, without the seal.

## 5. Open books and contributory accounting

**Our understanding.** The Foundation argues for moving beyond relying only on market prices, towards open book accounting and ways of recognising contribution that money misses.[^11]

**What we chose, and why.** Inside an organisation, the books are open to every member: anyone can read them, every loan and what's free to spend, and money recorded on someone's word is open to question for a week. Pay shares a period's earnings by weights the organisation sets for itself: hours given, seats held, contribution as the organisation's own peers see it, and equal shares. Revenue booked to a branch is never a basis for pay, so the people who care, sense and hold the work aren't starved by those whose work happens to show up as income. Under all of it sits a floor, an equal amount for each member, paid first. As built, the floor comes from each period's profit, so a lean month can leave it empty; we're changing it to come from what the organisation has free, capped so it can never pay out more than is there.

Beyond its own members, each organisation chooses how open it is to everyone else in the network: how far anyone in the network can explore it and read it, set for the whole organisation and branch by branch, up to and including its books. We're building towards that. Some of it is already there: a branch can publish what it keeps to the open web, or to named partners with a key, and offer its services and needs publicly or to organisations it chooses. We left the choice with each organisation, because how open to be is part of what makes an organisation itself. What isn't designed yet is openness as a shared practice across a network, such as open supply chains.

**How we think it lines up.** Well within an organisation. Across a network, as far as each organisation chooses to open itself.

**Where we might be wrong.** Leaving openness to each organisation may mean most choose little of it, and open books across a network may need to be the default rather than a choice. And contribution as peers see it becomes something worth gaming once it carries any share of pay.

## 6. Cosmo-localism

**Our understanding.** The motto is "what is heavy should be local, and what is light should be global and shared."[^12]

**What we chose, and why.** Land, money, liability and people stay with each organisation. Patterns, starter packs and improvements to the code travel. A network keeps a thin balance sheet: agreements and shared code, not land, because anything holding everyone's assets becomes a target. The Steward isn't the network, and nothing it holds stops an organisation from operating. For networks of physical sites we've sketched ideas borrowed from the commons world: the Mietshäuser Syndikat's lock against selling a site off, mutual credit between organisations on the WIR model, and a record of contribution inside a community that doesn't turn sharing into trading.[^13] These are sketches, not things we've built.

**How we think it lines up.** Closely, in its shape.

**Where we might be wrong.** A network that holds almost nothing may be too thin to do what the commons needs done together, and the physical-site sketches haven't met a single real site yet.

## 7. Commons infrastructure

**Our understanding.** The Foundation's recent work looks at protocols and shared ledgers as commons in their own right, held globally, with governance kept close to the communities that use them.[^14]

**What we chose, and why.** The operating system runs on the Internet Computer because no one party can switch an organisation's software off there, own it, or shut it down by seizing a server or leaning on an owner. DFINITY, the foundation behind it, describes what runs there as tamperproof and unstoppable.[^15] We think it's safer than any cloud host we know. It isn't a token economy: there's no token in the code, and the operating system never holds or moves an organisation's money. It reads the organisation's own books and governs how that money is allocated. AI models and email sit outside the chain, so a thin gateway, the stoma, carries that traffic. It holds nobody's data at rest, its source is given freely, and an organisation can run its own; on The Grove the Steward runs one shared stoma for everyone, because that's easier.

**How we think it lines up.** Strongly, but not absolutely. No host is beyond its own governance, and that's as true of cloud providers as of chains; a cloud provider can close an account on its own. The Internet Computer is governed by a vote of those who've staked its token. That vote can't reach into an organisation's own governance or change its decisions. What it can do, through a slow and public process, is take one unit of software off the network: a kind of proposal exists that can uninstall a canister's code, and in December 2021, after a copyright complaint about content hosted on the network, a proposal to remove one was raised and argued over in public.[^16] So the remaining risk is a single organisation being taken off the network by a public vote, not the network being shut down. The operating system's core is ordinary code with the chain kept at the edge, so in principle it could move.

We'd be open to running on commons infrastructure instead, or as well. Co-operatively owned hosting exists, Hostsharing in Germany and the Co-op Cloud network among others, and so do agent-centric systems such as Holochain that need no central host at all.[^17] What we'd want from any of them is what we chose the Internet Computer for: that no one party, the host included, can switch an organisation off.

**Where we might be wrong.** We haven't yet found another host we'd trust as much, so "it could move" is untested. And the infrastructure isn't held by the organisations that run on it; it's governed by the chain's own token holders, a different community with different interests.

## Where things stand

| The idea | How we think it lines up |
|---|---|
| Three institutions | Closely: organisations, a network nobody owns, and a Steward that is itself an organisation from go-live. |
| Generative, not extractive | By design: money can't buy a say, nothing an organisation needs is held by the network, the Steward earns from its own services, not from what passes between organisations. |
| Oriented to the common good | Strongly: guardrails in the core that can't be voted away. |
| Stakeholder governance | A different road, by choice: the advice process, not stakeholder seats. Those who depend on something are protected. |
| Reciprocity | Partly: a bounded commons, shared with the committed and credited by origin. The licence is open. |
| Open books, contributory accounting | Within an organisation, yes. Across a network, as open as each organisation chooses, for the whole and branch by branch. |
| Cosmo-local | Closely in shape; models for physical sites are sketches. |
| Commons infrastructure | Strongly but not absolutely: a public vote of the chain could take one organisation off it; it can't touch an organisation's governance or shut the network down. |

## Where we're least sure

None of this is an open commons, and we don't claim it is. These are the choices we're least sure of. We'd rather you pushed on our reasoning than took our word for it.

1. **The bounded commons.** We sealed the code to protect against capture. We may have protected it from the very people a commons should be open to.
2. **The advice process over stakeholder seats.** We chose decisions by the people closest to the work, with everyone affected heard first. That may leave the people around an organisation with too little say.
3. **The Steward's margin.** Without it there's no Steward, and without a Steward the code would have to be open to anyone, guardrails and all. We think the cost of leaving keeps it honest. With one network and one Steward, that discipline is mostly theoretical for now, and a paid guard is a risk in its own right.
4. **Openness left to each organisation.** Each organisation chooses how explorable and readable it is to the rest of the network, because how open to be is part of what makes an organisation itself. A commons may need more of it as the default.
5. **A thin network.** The Steward isn't the network, and the means to work together lives in each organisation's own copy of the operating system. Once each organisation holds its own side of its services and agreements, which we're building towards, there's nothing central to seize. A network that holds almost nothing may not be able to hold much in common, either.
6. **Trusting the host.** We chose the Internet Computer because no single party can switch it off. Its own governance can't touch an organisation's decisions, but a public vote could still take one organisation off the network.

And if we've misread the Foundation's ideas anywhere on this page, please tell us. We'd rather be corrected than be generous to ourselves.

If you'd like to go further, these chapters say more: [Chapter 1, A society of sovereigns](a-society-of-sovereigns.md), on what sovereign means here; [Chapter 6, Why an operating system](why-an-operating-system.md), on the guardrails and the Internet Computer; [Chapter 17, Money and value](money-and-value.md), on the commons, the floor and pay; [Chapter 25, Between organisations](between-organisations.md), on services and agreements; [Chapter 26, DNA, the network, and why not open source](dna-the-network-and-open-source.md), on the sealed code and the Steward; and [Chapter 27, Growing a sustainable network](growing-a-sustainable-network.md), the strawman for physical sites.

---

## Notes and further reading

[^1]: P2P Foundation, "About", blog.p2pfoundation.net. Its official name is the Foundation for P2P Alternatives (Stichting Peer to Peer Alternatives), registered in the Netherlands.
[^2]: Bollier, D., "P2P Foundation wins Golden Nica, Prix Ars Electronica", bollier.org, quoting the Foundation's description of itself as an "organized network".
[^3]: Bauwens, M. (2012), "Blueprint for P2P Society: The Partner State and Ethical Economy", *Shareable*; and "Three Institutions of Peer Production", P2P Foundation Wiki.
[^4]: Bauwens, M., Kostakis, V. and Pazaitis, A. (2019), *Peer to Peer: The Commons Manifesto*, University of Westminster Press. On generative and extractive ownership: Kelly, M. (2012), *Owning Our Future: The Emerging Ownership Revolution*, Berrett-Koehler.
[^5]: Chapter 26 describes the Steward, how releases are adopted, and the sealed code.
[^6]: The guardrails, in short: trust is given by peers, never by yourself and never bought; trust given on doesn't pass on again; delegated votes are equal and lapse if unused, and fade; trust and money are kept apart, with no way to turn one into the other; money carries no say; value tied to a purpose can't be taken out of it; the Clearing stays off the record; decisions commit only with enough of the forum behind them and after any concern has been heard; and the floor comes first, an equal amount for every member present, which work never feeds.
[^7]: Bauwens, M. and Kostakis, V. (2014), "From the Communism of Capital to Capital for the Commons: Towards an Open Co-operativism", *tripleC*, 12(1). See also "Why We Need a New Kind of Open Cooperativism for the P2P Age", P2P Foundation Wiki.
[^8]: On the advice process in self-managing organisations: Laloux, F. (2014), *Reinventing Organizations*, Nelson Parker. On consent in sociocracy: Rau, T. J. and Koch-Gonzalez, J. (2018), *Many Voices One Song*, Sociocracy For All.
[^9]: The record of who depends on what checks that a landing is attached, not that it's good enough. Something locked to the purpose can't yet be sold, given away, scrapped or written off at all; it can only be moved, and stays locked.
[^10]: Kleiner, D. (2010), *The Telekommunist Manifesto*, Institute of Network Cultures, which carries the Peer Production License drafted with John Magyar. "CopyFair License" and "Commons-Based Reciprocity Licenses", P2P Foundation Wiki. Vieira, M. S. and De Filippi, P. (2014), "Between Copyleft and Copyfarleft: Advanced reciprocity for the commons", *Journal of Peer Production*.
[^11]: "Ten Commandments of Peer Production and Commons Economics" (2015), Uncommons conference, Berlin, P2P Foundation Wiki: open supply chains and open book accounting as ways of coordinating beyond price signals.
[^12]: "Introduction to Cosmo-Localism", P2P Foundation Wiki. Kostakis, V., Niaros, V., Dafermos, G. and Bauwens, M. (2015), "Design global, manufacture local: Exploring the contours of an emerging productive model", *Futures*, 73, 126 to 135. Ramos, J., Bauwens, M., Ede, S. and Wong, J. (eds) (2021), *The Cosmolocal Reader*, Futures Lab.
[^13]: Chapter 27, Growing a sustainable network. Mietshäuser Syndikat, Freiburg, early 1990s; WIR Bank, Switzerland, 1934. On governing shared resources: Ostrom, E. (1990), *Governing the Commons*, Cambridge University Press.
[^14]: "Michel Bauwens on Technological Sovereignty in the Transition from a Marxist Capitalism to a Proudhonian Capitalism", P2P Foundation Wiki, on platform co-ops, ledger co-ops and cosmo-local protocol co-ops.
[^15]: Internet Computer, internetcomputer.org, which describes apps hosted there as "tamperproof, unstoppable, and sovereign".
[^16]: DFINITY forum, "Upcoming proposal and discussion on content moderation" (December 2021), and "Nintendo Incident: Feedback Summary and Open Questions". Internet Computer, "Proposal Topics and Types", learn.internetcomputer.org, on the proposal type that uninstalls a canister's code.
[^17]: Hostsharing eG, a hosting co-operative owned by its members, hostsharing.net. Co-op Cloud, an open-source platform for co-operative hosting, coopcloud.tech. Holo and Holochain, holo.host. See also "Cooperative Community Cloud", P2P Foundation Wiki.
