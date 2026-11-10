# Measured against the research on self-managing organisations

<!-- card: The operating system weighed against the evidence: Harvard's field experiment, the six problems every organisation must solve, and Buurtzorg at scale. -->
<!-- description: Most writing on organisations without bosses is advocacy. Here we weigh an operating system for them against the research: Lee and Edmondson's definition, Lee's case study and field experiment, Martela's six problems of organising, and Buurtzorg at fourteen thousand people. -->

*A working draft, November 2026; expect it to change. One of a series weighing what we've built against the work of people whose thinking we respect.*

---

**In this page**

- What's being measured: an operating system, the networks of organisations running it, and The Grove, the first of them
- Our understanding of four pieces of research on organisations without managers, which we'd welcome being corrected on
- Seven tests from that research in turn: what we chose, why, how we think it lines up, and where we might be wrong
- The findings that are hardest for us, and the places we're least sure of

---

Most of what's written about organisations without bosses is advocacy. Michael Lee, whose doctoral research at Harvard Business School is the centre of this page, says much of the practitioner rhetoric can be "hyperbolic, promising occupational nirvana".[^1] A researcher in this field should arrive at a book like this one expecting more of the same: a design by people who already believe, checked against nothing.

So this page is different from the others in the series. Those weigh the design against a body's ideas. This one weighs it against evidence, including a twelve-month field experiment that found no average benefit to people from taking decision authority away from their managers, and harm to some.

We don't try to argue that away. We set out what we chose, why, and how we think it lines up, so that people who do this research can test our reasoning and tell us where it fails.

## What's being measured

Three things, and it helps to keep them apart.

**The operating system** is the software an organisation runs: the rules for seats, decisions, trust, money and work, with a few guardrails at its core that nobody inside an organisation can vote away. It has no name of its own. We're building towards each organisation running its own copy; as the code stands, the simulated organisations share one space. Its guide inside every organisation is an AI companion called Wise-Eye.

**A network** is organisations running the operating system that recognise one another and share agreements. Each network has a **Steward**: an organisation that looks after the network's code and ships its releases.

**The Grove** is the first such network. It's still being built and tested, and its organisations today are simulated: seeded, grown and run by AI people. Nothing on this page has been tested with real organisations. That matters more here than anywhere else in the book, because this page is about evidence, and we have none of our own yet.

Three words used below. An organisation's work is held in **branches**: parts of the organisation shaped around a piece of work, each with a purpose and the things it answers for. Each branch has a seat, held by a **steward**. And decisions are made in **forums**. A branch is governed in one forum: the stewards of its parent and of its sibling branches, with the branch's own steward taking part as a person. The root has no parent, so it's governed by its own stewards and the stewards of the branches grown directly from it.

We keep to the rule the rest of the book follows: *is* only for what's built, *building towards* for what's decided but not built, and *we don't know* for what's open.

## Our understanding of the research

This is how we understand four pieces of work. If we've got any of it wrong, we'd like to be corrected, and we'll change the page.

**Lee and Edmondson (2017)** reviewed decades of research on organising with less hierarchy and gave the field a working definition. A self-managing organisation is one of those that "radically decentralize authority in a formal and systematic way throughout the organization".[^2] Amy Edmondson chaired Lee's doctoral committee at Harvard Business School.

**Lee (2019)**, his doctoral dissertation, adds two studies to that review.[^3] One follows, for a year, a payments company of about a hundred and twenty-five people that had adopted Holacracy, asking how it coordinated without managers. The other is a twelve-month field experiment in the State of Washington's technology agency, asking whether taking decision authority away from managers improves people's sense of power, engagement and satisfaction, and for whom.

**Martela (2019)** asks what's actually new about self-managing organisations. He takes four problems every organisation must solve, from Puranam, Alexy and Reitzig, splits two of them, and compares how bureaucracy, adhocracy and self-managing organisations solve all six: dividing tasks, allocating them, rewarding, stopping freeriding, giving direction and coordinating.[^4]

**Martela and Nandram (2025)** describe Buurtzorg, the Dutch home-care organisation with over fourteen thousand people in more than nine hundred teams, two directors and no middle managers.[^5]

From these we've drawn seven tests:

1. **The definition:** authority decentralised radically, formally and throughout.
2. **Dividing and allocating the work,** with no manager to do either.
3. **Rewards and freeriding,** with no manager to judge or to watch.
4. **Direction and coordination,** and what replaces the manager who carried information.
5. **Clear and dynamic role boundaries,** the thing Lee found working, and its four costs.
6. **Who it helps and who it harms,** the finding of Lee's experiment.
7. **What stays at the centre, and where it fits:** strategy, joining and leaving, scale.

None of these authors certifies anything, so this isn't a compliance check. It's our own reading, and it may be a generous one. That's what the sections on where we might be wrong are for.

## 1. The definition

**Our understanding.** Three features make a self-managing organisation. The decentralisation is radical: the reporting relationship between manager and subordinate is gone, and nobody's decision rights can be overridden by someone because they're the boss. It's formal: written into explicit rules, because hierarchy "cannot easily be altered by simply declaring it absent", and authority that's merely delegated gets taken back in a conflict or a crisis.[^6] And it runs throughout the organisation, senior people included. Lee is careful about what this doesn't mean. Managerial work still has to be done by someone. Some roles still carry more authority than others. Informal hierarchy survives. What's gone is any formal relationship in which one person holds power over another's autonomy.

**What we chose, and why.** There are no reporting relationships in the operating system at all. Nobody is anybody's manager, and nothing in it lets one person direct another's work. Authority sits in seats and forums. Every change to an organisation's structure is a proposal, decided by consent in a forum, with the weight behind each voice given by peers and taken back by them. The founder holds no override: the root is one seat in a forum, like any other. And the rules are as formal as rules can be. They're code, the same in every organisation, with guardrails no forum can vote away. We chose that because we'd seen what Lee describes: empowerment that depends on a manager's goodwill ends when the goodwill does.

**How we think it lines up.** We think it meets all three features, and goes further than the cases Lee studied on the second. In those, the rules were a document people ratified. Here they're the system the organisation runs on, so there's no gap between the rules and the tool.

**Where we might be wrong.** Three places. First, the rules only bite once a second person holds a seat. Until then one person decides the structure, the money and who is seated, and members can only advise. Nobody's work is being directed, because only people who hold seats carry work. But a founder who is slow to seat anyone keeps every decision, and the design shows that plainly without preventing it. Second, branches form a tree, and a forum higher up can change or close a branch below. That's a forum deciding, never a person, but it's still a hierarchy of parts, and someone who holds a branch above may step in when a promise below is at risk. A researcher could fairly ask how different that feels from a manager on a bad day. Third, giving trust the status of weight in decisions may harden the informal hierarchy this research warns about, even though peers can take their trust back any day. We've designed trust to fade unless it's renewed, and that part isn't running yet.

## 2. Dividing and allocating the work

**Our understanding.** In a bureaucracy, managers break the goal into tasks and hand them down. In a self-managing organisation, Martela says, individuals have both the responsibility to spot what needs doing and the authority to make it part of the structure, and people have considerable say over which roles they take.[^7] That asks a lot. People have to be proactive, and committed enough that the unattractive but necessary work still gets done. Where work is tightly linked, something explicit is needed so that every necessary task ends up with someone. His example is Morning Star, where each person negotiates written agreements with the colleagues their work affects.

**What we chose, and why.** Anyone can raise a tension, and a tension can become a proposal for a new branch, a changed purpose or a new thing a branch answers for. Branches are born from work that keeps arriving, with evidence, so the structure follows the work. For allocation, work belongs to a branch, never to a person. Everything that arrives comes through one door and is routed to whichever branch has said it answers for that kind of work. Work that fits nowhere goes to the root, so nothing is left without a home. Seats are offered, not assigned: an open seat is posted, members say they'd like it, someone else proposes them, and the forum decides. A step where the person named says yes isn't built yet. An empty seat passes its weight to the branch above until someone steps in. And a promise made to someone outside always belongs to a branch and is carried by a named person, with a day on it.

**How we think it lines up.** Closely on division, which is bottom-up by proposal as Martela describes. On allocation we've gone a different way from his examples. People don't pick from one pool across the organisation, and they don't negotiate contracts with each other. The work finds the branch, and inside it whoever holds the seat picks it up. We think that covers his test that every necessary task ends up with someone, including the dull ones, because work a branch leaves or refuses rises to the branch above and never disappears.

**Where we might be wrong.** Routing by what a branch has written down depends on the writing being good. Lee's case shows the failure: once roles were written, some people refused anything not in them. We take that up in section 5. Work with no home is meant to be a tension, not a burden. It shows where it rests, and a tension becomes a proposal: a new thing a branch answers for, or a new branch. Most of it should be given a home long before it reaches the root, and what does reach the root is there for the root to grow structure for, not to do. That's the design. What's untested is whether a busy root does the proposing or quietly does the work.

## 3. Rewards and freeriding

**Our understanding.** With no manager to set pay, Martela expects peers to do it, as at Morning Star and Valve, and he expects heavier reliance on work being rewarding in itself. With no manager to watch, he expects peers to monitor each other's performance, with explicit steps for resolving conflict and people skilled enough to use them. He's blunt about the stakes: without a way to deal with freeriding, cooperation declines.[^8] Buurtzorg does it differently from his prediction on pay, following the national agreement for its sector with no bonuses, but relies heavily on visibility. Every visit is recorded, each nurse can see what teammates have done, and a dashboard compares each team with the rest.[^9] The research also carries a warning. Peer control in self-managed teams has been found to become as coercive as a manager's.[^10]

**What we chose, and why.** Pay is a share of what the work earned, divided by a rule the organisation agrees by proposal in its root forum. The rule is a set of dials: how much goes by hours given, by roles held, by contribution, and in equal shares. Beneath that an organisation can set an equal floor for every member. Nobody's pay is set by a person above them. Trust and money are kept apart as two currencies, and neither converts into the other.

On freeriding we've chosen something the research might not expect. The operating system publishes no score on any person. There are no ratings, points, rankings or comparisons on show, and the organisation's reading of itself has no place for a person's name. Two things are held about a person: the trust peers have given them in a forum, and a private picture of skill that decides only who is asked for advice. Neither is published or ranked.

What's visible instead is the work, and everything a person touches in it: what each branch answers for, every promise and its day, who carries it, and what's waiting on each person, said as what waits and never as a judgement. A promise that slips rises as a message to the branch above, where someone may step in. And the consequences are real. Peers can take back the trust they've given someone, which takes away their weight in decisions. And a forum can hand a seat to someone else by proposal.

**How we think it lines up.** On rewards, partly. Nobody decides anyone's pay. The people in the root's forum agree one rule for everyone, by proposal, and each person's share then follows from the record: hours given and roles held. So peers set the rule, which is less than Martela's peers judging each other. The exception is the contribution dial, where an organisation turns it up. On freeriding, closer than it first looks. Martela expects peers to monitor performance and to have a way to act. Here the work is open for peers to see, and peers hold both sanctions: trust and the seat. What we've refused is turning that into a published number, because of the warning this research itself carries about peer control, and because we think people hide what's scored.

**Where we might be wrong.** If the research is right that cooperation declines without a sanction, the question is whether ours bite soon enough. Trust withdrawn and a seat handed on both need peers to act, and peers are often slow to. A member who holds no seat has neither to lose. The contribution dial, which is off unless an organisation turns it up, follows how peers see each person's contribution, and we haven't shown that this stays clear of the rating we've refused. A way to exclude someone who's acting in bad faith is something we're building towards; it isn't there yet. And making everything a person touches visible is peer monitoring, whatever we call it. The research's warning about that applies to us too.

## 4. Direction and coordination

**Our understanding.** If people are to make decisions a manager used to make, they need the information a manager used to hold. Martela's rule is that when decisions are decentralised, information must be too, finances included, and people need to be able to read it. For coordination between teams, with no hierarchy to fall back on, he sees two answers: people given the job of linking, and information systems that track who's responsible for what and are open to everyone. Those systems, he says, have taken over much of the coordinating, progress-tracking and information-sharing that managers did.[^11] Buurtzorg bears him out. Its purpose-built system was designed with nurses, because existing ones served the administration and not the people doing the work.[^9]

**What we chose, and why.** This is the centre of what an operating system is for. The organisation's purpose is held at the root and every branch has its own, so direction is written where everyone can see it. A founder's vision enters as bets, each saying what would show it wrong. The organisation reads its own state from a ledger of work at each branch, open to everyone in it: which branches are growing or withering, where work keeps passing between them, where it's drifting from what people say. Between branches, coordination happens through the routing of work, through conversations between branches, and through promises. And Wise-Eye sits beside every seat, reading the same records the organisation keeps, routing what arrives, drafting replies and saying what's at risk. It advises and drafts, and where a person has granted it, it sends low-stakes routine work by itself. It never decides a proposal.

**How we think it lines up.** This is where we're most confident. Martela's claim that information systems can take over the manager's coordinating work is close to the premise of the whole design, and the transparency he asks for is the default.

**Where we might be wrong.** Open information is only useful to people who can read it, and Martela expects self-managing organisations to need more educated people for that reason. We're leaning on Wise-Eye to close that gap, and we don't know that it will. Money is where we're thinnest: an organisation's books sit beside its bank, and how well an ordinary member can read them is untested. And an AI that drafts and routes for every seat could become the manager nobody appointed. It can't decide a proposal, but what it chooses to show is a kind of power.

## 5. Clear and dynamic role boundaries

**Our understanding.** This is Lee's most useful finding, and it runs against the usual picture. The standard idea of the organisation after bureaucracy is loose and informal: remove the hierarchy, blur the roles, let people adjust to each other. Lee found the opposite working. The company he studied removed managers' authority and made roles more formal, not less. In three months the number of written roles more than doubled, with no more work being done. It was existing work being written down. Roles were visible to the whole company on a shared platform and revised constantly, by anyone, through a process where a proposal passed unless someone showed it would cause harm.

Two things followed. People coordinated directly, role to role, without going through a manager. And clear boundaries protected people. Junior people could say no to senior ones by pointing at the written role, and senior people used the boundaries to hold themselves back. Lee calls clear boundaries "a bulwark against the tendency of power to centralize", and the company "a dynamic and empowering variant of bureaucracy".[^12] He's exact about what made formality freeing. Roles were set by the people closest to the work, with authority equal to responsibility. They were visible to everyone. And they were easy to change.

He's equally exact about the costs, and names four. People attended to their own roles over the whole, and moving anything across roles got harder. Written roles crowded out shared values: challenges were met with "That's my role". It turned impersonal: one person said "The new system is pretty cold", and some used the formal process to avoid a direct conversation. And constant change brought confusion and overload.

**What we chose, and why.** Branches are our version of this, and we reached it for the same reason: when nobody has written down which part answers for what, somebody ends up handing out the work. Each branch has a purpose, the things it answers for, and its working practices, written down, and every member can see the whole tree. They're changed by proposal in the forum around the branch's parent, by consent, with a concern being a reason the change would do harm and not a preference.

**How we think it lines up.** On Lee's three conditions, closely. Set by the people around the work, visible to all, and revisable by a low-threshold process: those are all in the design. Two of our choices bear on his costs. A branch is shaped around a piece of work with its own purpose, and the organisation's purpose sits at the root, so the "why" is written beside every "what". That's aimed at roles crowding out values. And changes to structure run on clocks, with high-impact ones waiting before they take effect, and each one looked back on. That's aimed at churn.

**Where we might be wrong.** His first cost has two parts, and we've answered one. Everyday work that crosses branches doesn't follow the tree. Work is routed to whichever branch answers for it, anywhere in the organisation. One branch can ask another for something by a day, and that ask is held like any promise. A customer's matter stays on one thread however many branches it touches. So the routine case is covered. The harder part is the one Lee's manager described: someone who once had to persuade a couple of people found forty to bring along, and building anything new across the organisation got harder. A design made of branches that each answer for their own work invites that. Our answers are the shared reading, tensions that climb to a forum that can act, and the Field where people sense together. None of them has been tested against a real cross-cutting push. On coldness, we've added a gathering that's kept off the record, and a companion whose advice is there to be heard, never obeyed. Whether a system can be made warm by design is a fair thing to doubt. Lee also warns that people may stop noticing written roles after the first year. We think that risk belongs to roles kept as a map beside the work, which people have to remember to consult. A branch isn't a map. It's where the work arrives, so there's nothing to forget to look at. If what a branch says it answers for goes stale, work stops finding it and shows up with no home, which is how the staleness gets noticed.

## 6. Who it helps and who it harms

**Our understanding.** Lee's experiment is the hardest evidence on this page. In the State of Washington's technology agency, groups covering about half of five hundred people opted in; some were given a group-level version of Holacracy for twelve months and the rest kept their managers, with a training on encouraging participation. On average it made no difference to how empowered, engaged or satisfied people were. But it wasn't nothing for everyone. The effect was more positive for people their managers had rated as high performers, for people who'd wanted it, and for people in groups where it already felt safe to speak up, and it turned negative for some of the opposite groups. The pattern was clearest for performance: high performers gained on all three measures and low performers lost on all three. Lee's conclusion is that decentralising authority "can do harm as well as good", and that it's "not a panacea nor for everyone".[^13] He suggests two reasons for the harm: the new way of meeting added work, and the experiment "raised expectations for some without changing their reality".

We should say what the experiment wasn't. Groups chose to take part, and only nine of the thirty-nine were assigned at random. The groups sat inside an agency that otherwise kept its hierarchy, which Lee calls an artifact of the design; by his own definition, we'd add, they weren't a self-managing organisation. And the agency was still unsettled after a merger, with a budget shortfall found part-way through. He calls it a conservative test. We'd call it the best evidence there is, and take it seriously.

**What we chose, and why.** Little in the design was chosen with this finding in front of us, and we'd rather say so. But one choice bears on it more than any other. Lee's groups were handed a new process to run: new meetings, new rules for changing roles, and the job of working out what to do with their new authority. He gives that added work as one reason some people ended up worse off. Here the mechanism is in the operating system, not in meetings. There are no governance meetings to learn. Work arrives already routed to the branch that answers for it, often with a reply drafted beside it. A decision arrives as a proposal to consent to or raise a concern about, with its evidence attached. So what reaches a person is close to: here's what's yours, and here's the next step. Our bet is that this suits people who like clear work in front of them as well as those who like to roam, and that it asks less of the proactivity Martela says self-management needs.

Other choices bear on it too. Joining is by personal invitation from someone who holds a seat, so nobody is put into an organisation like this who didn't choose it. Seats are offered and not assigned, and a member can belong without holding one. Beneath pay an organisation can set an equal floor that isn't earned by work; it starts at nothing, and a floor no forum can vote away is something we're building towards. And before The Grove goes live, the way in is a sandpit: time spent in a simulated organisation, so people can find out whether they want this before anything depends on it.

**How we think it lines up.** Lee's three conditions are interest, performance as rated by managers, and a safe climate. On interest, the design selects for it, which is what Buurtzorg did: many of its nurses left other employers to join.[^9] On performance, we're betting that work which finds its branch, and a companion beside every seat, lower what self-management asks of a person. On climate, we have an off-the-record space and no published scores, and that's all. And the two reasons Lee gives for the harm he found, a heavier way of meeting and a self-managing group stranded inside a hierarchy, are both things the design avoids.

**Where we might be wrong.** Our bet is untested, and Lee's finding is a reason to doubt it. He cites the view that self-management needs "a higher level of psychological development and interpersonal skill",[^14] and his experiment suggests it amplifies whatever is already there. People in a team that feels unsafe before are likely to end up less engaged and less satisfied, and no rule in software repairs that. Making the work simpler may not be what his low performers needed; we don't know what they needed. A companion might equally let capable people run further ahead. Selecting for people who want it is honest, but it narrows who this is for. And one tempting path is the one Lee's experiment warns against: a self-managing team inside a company that otherwise keeps its bosses. His result says to be very careful there.

## 7. What stays at the centre, and where it fits

**Our understanding.** In the best-known cases, two things were decentralised least. Strategy stayed with the chief executive at Zappos and Morning Star, and Valve's executives made the biggest calls. Hiring and firing weren't decentralised at Zappos, were driven by work groups after consulting influential leaders at Morning Star, and ended with the chief executive at Valve.[^15] Buurtzorg's teams do their own hiring. At Buurtzorg, top management holds strategy, the design of the organisation and dealings with insurers and government, tested through the founder's blog, where a proposal might draw hundreds of comments. Its coaches are worth noting. Each supports forty-five or more teams, and it's made explicit that they have "no decision-making authority".[^9]

On fit, Martela names three conditions: units that don't depend much on each other, work that's tailored and not standardised, and skilled, motivated people. Buurtzorg has all three, and it scales by adding small teams that barely need one another, splitting any that pass twelve people. Elsewhere, the record is thinner. GitHub ran without bosses to a few hundred people and then brought managers in. Zappos's staff turnover rose by half the year it adopted Holacracy in full. Lee expects limits to scale and notes that crises tend to pull authority back to the centre. Martela's own verdict on whether this is the future is that it's "too early to say".[^16]

**What we chose, and why.** We decentralised both of the things the cases held closest. Purpose is held at the root and changed only by proposal in the root's forum; a founder's strategy enters as bets that the organisation tests. People join by personal invitation from someone who holds a seat, and in a newcomer's first month other seat holders can question the invitation. Seats are given and handed on by forums. Nobody can be fired by a person: peers withdraw their trust, and a forum can pass a seat on. Anyone can leave at once, with no permission. We did this because a design that keeps strategy and membership at the top has kept the two decisions that most make someone the boss.

**How we think it lines up.** Here we've gone further than most cases in this research on strategy, which means we have the least evidence behind us. On crisis, Lee's point lands directly. We've designed an alarm for emergencies, with no override, and it isn't built. Until it is, the honest answer to "what if the building's on fire?" is that the people in it act and the operating system catches up.

**Where we might be wrong.** Strategy may resist decentralising for good reasons. Martela notes it's hard to imagine a division voting to abolish itself. A forum weighing bets may be slower and more timid than one person with a view. On fit, everything we've tested is simulated, and most of it small, which is the easy case by Martela's conditions. Tightly linked work, low-skill work and thousands of people are all untested. Buurtzorg's lesson is that scale came from modularity, and we don't know whether branches give the same thing. And we have nothing like its coaches: experienced people with no authority who help a team that's stuck. Wise-Eye isn't that. A network could offer it, organisation to organisation, but nothing in the design provides it.

## Where things stand

| The test | How we think it lines up |
|---|---|
| The definition | Meets all three features, with the rules in code. The rules bite only from the second seat, and branches form a tree: those are the soft spots. |
| Dividing and allocating work | Division is bottom-up by proposal. Allocation is by routing to branches, not by choice or contract. |
| Rewards and freeriding | One pay rule for everyone, agreed in the root's forum. The work is open and peers hold the sanctions, with no published score. Whether those sanctions bite soon enough is open. |
| Direction and coordination | Our strongest ground: open information and a system that does the coordinating work. Financial literacy and the companion's quiet influence are open. |
| Clear and dynamic role boundaries | Lee's three conditions are in the design. Everyday work crosses branches freely; a new cross-cutting push is untested. |
| Who it helps and who it harms | Selects for interest, and puts the mechanism in the system so people aren't running a process. A bet, with no evidence yet. |
| The centre, and where it fits | Goes further than any studied case on strategy and membership. Crisis, scale and tightly linked work are untested. |

## Where we're least sure

These are the choices we'd most like people who do this research to push on.

1. **No published score.** The work is open and peers can withdraw trust or hand a seat on, but nothing rates a person. If freeriding needs a quicker or sharper answer than peers choosing to act, this is wrong.
2. **Making it easy in place of making people ready.** We're betting that work which arrives routed, decisions that arrive as proposals, and a companion beside every seat lower what self-management asks of people. Lee's experiment says who thrives depends on performance, interest and safety. We have no evidence our bet changes that, in either direction.
3. **Strategy and membership held by forums.** The best-known cases kept strategy at the centre, and most kept the last word on hiring and firing there too. We may have decentralised the two things that most need a single mind, or the two that most make a boss.
4. **Branches against the whole.** Writing down what each part answers for is what Lee found working, and what he found making new cross-cutting work harder. Everyday work crosses our branches freely. A push that needs many branches to move together is untested.
5. **Formality in code.** Rules that are the system can't be quietly ignored. They also can't be bent by a group that has good reason to, except by leaving the network, which is designed and not yet built.
6. **All of it on simulated organisations.** Everything here is design and rehearsal. This research is a year in one company, one experiment and a handful of cases, and it's still far more evidence than we have.

And if we've misread this research anywhere on this page, please tell us. We'd rather be corrected than be generous to ourselves.

If you'd like to go further, these chapters say more: [Chapter 7, The spark](the-spark.md), [Chapter 9, The branch](the-branch.md), [Chapter 11, Making decisions](making-decisions.md), [Chapter 12, Trust](trust.md), [Chapter 13, Work that finds its way](work-that-finds-its-way.md), [Chapter 15, Promises](promises.md), [Chapter 17, Money and value](money-and-value.md), [Chapter 19, The read](the-read.md) and [Chapter 22, The co-pilot](the-co-pilot.md).

---

## Notes and further reading

[^1]: Lee, M. Y. (2019), *Self-Managing Organizations: Exploring the Dynamics and Consequences of Radically Decentralizing Authority*, doctoral dissertation, Harvard Business School, p. 49.
[^2]: Lee, M. Y. and Edmondson, A. C. (2017), "Self-managing organizations: Exploring the limits of less-hierarchical organizing", *Research in Organizational Behavior*, 37, 35 to 58. The definition is also at Lee (2019), p. 14.
[^3]: Lee (2019), as note 1. The case study is Chapter 3 and the field experiment Chapter 4.
[^4]: Martela, F. (2019), "What makes self-managing organizations novel? Comparing how Weberian bureaucracy, Mintzberg's adhocracy, and self-organizing solve six fundamental problems of organizing", *Journal of Organization Design*, 8:23. The four problems are from Puranam, P., Alexy, O. and Reitzig, M. (2014), "What's 'new' about new forms of organizing?", *Academy of Management Review*, 39, 162 to 180, as Martela cites it.
[^5]: Martela, F. and Nandram, S. (2025), "Buurtzorg: scaling up an organization with hundreds of self-managing teams but no middle managers", *Journal of Organization Design*, 14, 227 to 237.
[^6]: Lee (2019), pp. 14 to 15, 34 to 35 and 40 to 43.
[^7]: Martela (2019), pp. 8 to 10.
[^8]: Martela (2019), pp. 4 to 5 and 10 to 13.
[^9]: Martela and Nandram (2025), pp. 228 to 235.
[^10]: Barker, J. R. (1993), as cited in Lee (2019), p. 24.
[^11]: Martela (2019), pp. 13 to 15.
[^12]: Lee (2019), pp. 105 and 106. The three conditions are at pp. 95 to 98 and the four costs at pp. 99 to 104.
[^13]: Lee (2019), pp. 149, 4 and 148. The results are at pp. 134 to 148.
[^14]: Lee (2019), p. 51.
[^15]: Lee (2019), pp. 38 and 168 to 169.
[^16]: Martela (2019), pp. 15 to 21, and Martela and Nandram (2025), pp. 228 and 234 to 235. The Zappos figure is Martela (2019), p. 18. On scale and crisis: Lee (2019), pp. 48 to 49.
