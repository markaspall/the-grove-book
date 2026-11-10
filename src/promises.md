# Chapter 15. Promises

*A working draft, November 2026. This book is being written while the operating system is being built; expect it to change. Checked against the build as it stood on 1 November 2026.*

---

**In this chapter**

- Why organisations without a boss are suspected of being soft on deadlines
- What a simulated bakery showed when promises had nowhere to live
- Why commitments get a firmer mode, firm on the promise and never on the person
- How a promise is carried, timed and raised when it's at risk, and who may step in
- What was left out on purpose, like alerts and timesheets, and why

---

Here's a doubt that usually arrives once people have warmed to everything else.

Self-management sounds lovely for deciding things. Purpose, proposals, who holds which seat: fine, talk it through, take your time, consent when you're ready. But a customer who was promised a delivery on Thursday doesn't care how gracefully you reached agreement. They care whether it arrives on Thursday. And the sceptic suspects, with some reason, that organisations without a boss are soft on exactly this. Nobody chases. Nobody is on the hook. Deadlines become gentle suggestions, and the people who keep their word end up quietly carrying the ones who don't.

It's a fair worry. Plenty of flat organisations have discovered it the hard way. Taking away the person who shouts about deadlines doesn't automatically put anything in their place.

## What a missed promise costs

The cost of a dropped commitment is easy to see from the outside. A customer waits, chases, waits again, and goes elsewhere. A partner stops trusting your dates and starts padding their own. Revenue leaks out in ways that never show up as a single line on a report, because each lost order looks like a small, separate accident.

The cost on the inside is quieter and lasts longer. When nobody can see who is carrying a promise, the conscientious people carry all of them, just in case. They lie awake over things that may already be in hand. Meanwhile someone else is swamped and nobody knows, because being swamped doesn't show on any screen. Then the date passes, and the hunt for whose fault it was begins. That hunt is the part people remember. It teaches everyone to promise less and hedge more.

The usual fix is a manager with a list. It works, up to a point. It also puts one person at the centre of every commitment, and that person becomes the thing everyone waits on, the familiar bottleneck.

## The bakery that lost its orders

Promises came late in the design. By the time we turned to them, on 20 October 2026, we had already built how organisations decide, how trust is extended, and how work finds the branch that answers for it (a branch being the part of the organisation that holds a particular kind of work). We thought commitments would follow naturally from all that. A simulation showed us they didn't.

We ran a model-played bakery organisation over many weeks: AI agents playing the people, customers sending orders, the whole thing running on the system as it then stood. In one run, a promise made to a customer landed on a branch with nobody carrying it. Its day came and went with nothing said. Two weeks later, several well-meaning helpers found it at the same moment, and every one of them wrote the same apology.

That wasn't a one-off. In that run, twenty-seven of sixty-seven orders were lost without an answer. Replies that had been drafted sat for days waiting on one approver, and nobody could see that this person was swamped. Helpers collided eleven times, each stepping in on work someone else had already picked up.

Nobody in that bakery was lazy or careless. The structure simply had no place for a promise to live. Everything invitational about the design, the openness, the absence of anyone handing out tasks, was doing its job. It was just the wrong mode for this kind of work.

## Two modes, one organisation

That was the turn for us. Being self-managing doesn't mean treating all work the same way. It means picking the right mode for each kind.

Purpose, sensing, proposals and structure stay invitational in an organisation on The Grove. They're about what we might do and how we might be, and they're better for being open. A commitment made to someone is different. Someone outside is relying on it. So it gets firmness: an owner, a date, a clock everyone can see, and a way of rising when it's at risk.

The firmness applies to the commitment, never to the people. Nobody is ordered to do anything. Nobody's standing goes down because a promise they carry is in trouble. What changes when a commitment is at risk is that more people can see it, and more people may step in.

Terry Winograd and Fernando Flores argued in the 1980s that much of the real work of organisations happens in conversations for action: someone asks, someone promises, someone declares it done, someone accepts.[^1] The promise is the hinge. Our job was to give it somewhere to sit.

## What changes in an organisation on The Grove

**Every promise belongs to a branch and is carried by a person.** The branch answers for it, so if the person moves on, the promise doesn't vanish with them. But a branch can't feel pressure, and a person can. So each promise is carried by someone, by default whoever made it. Anyone holding the branch can take the carrying over. If Wise-Eye, the AI companion, made a promise on its own, nobody carries it until someone takes it up. Once the branch knows how far ahead that kind of work usually starts, a promise nobody carries reads as at risk a day sooner, to leave time to find someone.

**The rhythm is learned, not guessed.** Many planning tools ask you to estimate up front how long each step takes. Organisations on The Grove don't. Once a branch has kept three or more promises of a kind, the system learns how far ahead the steps usually start and how long they take. Until then, it assumes nothing, unless the branch says for itself how far ahead a step starts. What the branch says comes first. An early version assumed every step started the day before the promise was due. That's a bakery's rhythm, not a law of nature, and we took it out.

**Each step has a latest start.** Worked back from the promise's day, every step has a point by which it needs to begin. A step reads as *starts by* a date, then *start today or tomorrow*, then *at risk* once its latest start has passed and nobody has it, or *stuck* if it's in someone's hands but untouched for longer than that kind of step usually takes, plus a day. And every card says what's at stake in plain words: if this doesn't start by Wednesday, the order promised to a named customer for Friday is missed. Not a red light. A sentence.

**Risk rises as a message, not a push.** When a step goes at risk or stuck, a message goes from its branch into the conversation of the branch above, once. If it goes overdue, it travels one branch further. Anyone holding a branch above may take a step that's at risk, stuck or overdue, even from a seat someone else fills. It says so on the work, where whoever had it will see it. This is what escalation means here: visibility plus permission, not authority. Nobody above gains the right to order anyone. They gain the right to help.

**Asks from outside run on a clock.** When someone outside the organisation asks for something by a day, the ask needs answering early enough for the work to be done. And if an answer is waiting for approval and goes at risk, someone holding the branch above may approve it. Whoever approves makes the promise. That's the cure for the swamped approver in the bakery.

**Load is visible.** For each person, anyone can see what waits on them: promises carried, work in hand, answers waiting on their approval alone. It's said as what waits, never as a judgement. There are no scores and no comparisons. If one person's load is keeping work waiting, and someone else has been doing that branch's work lately, Wise-Eye may offer to propose them to share the seat. An offer, never a move.

**There's a check before promising.** Before a promise goes out, it's compared with what's usual for its kind: its size, how much notice it gives, how loaded that day already is, whether the customer is new. Within the usual, Wise-Eye may send it as a low-stakes reply, once it has earned the right to send that kind. The first three promises of any kind always go to a person, because there's no usual yet. Outside the usual, a person approves, with the reasons shown. Agreeing a standing arrangement, the every-week kind, always needs a person. Once agreed, each next time comes round by itself.

**There's one state, not two.** When a promise is settled, its record card moves with it. Nobody updates a tracker and then updates a board.

**Changes stay human.** If a promise moves later, earlier, is cancelled, or the organisation asks to move it, that happens on the same promise, on its own thread, and a person approves it. Wise-Eye never changes or calls off a promise by itself.

It's worth naming what organisations on The Grove deliberately don't do. They don't assign people. They don't plan capacity, keep timesheets, set priorities from above or run sprints. Nothing sends alerts or reminders out to your phone or inbox. Taking a step is a way of saying *I can*. If you're away, you mark yourself away, and any promises you carry that fall in that time read as needing someone to carry them. Nobody has to notice you're gone for the work to notice.

## How we decided

The first question was who owns a promise. A manager, a rota and the branch as a whole were all possible. We chose whoever made it, because they're the one who feels its weight. Ownership passes only when someone else accepts it, never by decree. That keeps the invitational spirit intact even inside the firm mode.

The second was whether others could take overdue work out of someone's hands. This one took longer, because it can feel like a small violation. We said yes. Otherwise a promise could be locked to a person who's off sick, and the customer pays for the organisation's politeness. The work says who took it and from whom, so nothing happens behind their back.

The third was push notifications. They would have caught more slips. They'd also have turned the system into one more thing buzzing at people at dinner. We declined. Nothing is pushed outside; the work shows its state where the work lives. David Allen's point about getting commitments out of your head and into a trusted place shaped this, though we put the trusted place in the shared organisation rather than in one person's list.[^2]

We also chose to build promises as one complete piece rather than in slices. The bakery had shown how the parts depend on each other: visible load without rising messages helps nobody, and rising messages without permission to step in just spread the worry. Eliyahu Goldratt's work on protecting the whole chain rather than padding each step was in the back of our minds too.[^3]

What's uncertain is the obvious thing. This has been tested in simulation, not with real organisations. We don't yet know how it feels to have a step taken from you, however kindly. We don't know whether people will trust learned rhythms or want to override them. And we don't know whether a message into a branch conversation is loud enough, when the stakes are high and the room is busy. Those answers will come from the first organisations that use it.

## What you might take from this

Self-management doesn't have to be soft on deadlines. It can keep its openness for the things that benefit from openness, and give real firmness to the one thing that has someone outside depending on it: a commitment.

The firmness sits on the promise, not the person, and when a promise is in trouble the answer is more eyes and more hands, not more pressure.

Freedom and keeping your word aren't opposites; in a good organisation, each makes the other possible.

---

## Notes and further reading

[^1]: Winograd, T. and Flores, F. (1986), *Understanding Computers and Cognition: A New Foundation for Design*, Ablex. Their idea of the conversation for action, and of commitments as the basic unit of coordination, sits under this whole chapter.
[^2]: Allen, D. (2001), *Getting Things Done: The Art of Stress-Free Productivity*, Viking.
[^3]: Goldratt, E. M. (1997), *Critical Chain*, North River Press.

On promises as acts that change the world rather than describe it: Austin, J. L. (1962), *How to Do Things with Words*, Oxford University Press.
