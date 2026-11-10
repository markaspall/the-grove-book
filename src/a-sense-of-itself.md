# Chapter 21. A sense of itself

*A working draft, November 2026. This book is being written while the operating system is being built; expect it to change. Checked against the build as it stood on 1 November 2026.*

---

**In this chapter**

- Why a model that watches an organisation sounds like surveillance or a manager by another name
- What the organisation's hand-written instincts cost, and why the law stays exactly as it is
- What a learned sense of itself might feel, from strain and drift to work with no good home
- Why it senses and never acts, never pulls towards the average, and goes quiet where an organisation invents
- How organisations could learn together without handing over their records, and what we don't yet know
- How you could ask the organisation how it is, and how a network of them might read back something of society

---

A model that watches an organisation is either a surveillance tool or a manager by another name.

That's the doubt, and it's earned. Most software that claims to understand an organisation does it by watching people: who logged in, who replied, who's slow. And most software that claims to advise one ends up deciding, because a recommendation from a confident machine is hard to argue with in a busy week. Either way, something that sees everything has quietly become the boss.

This chapter is about something we're building towards and haven't built. None of it is in the product. It runs offline, beside the simulations, on simulated organisations only, and no organisation, simulated or real, is shown anything it says. We're writing about it now because the stance matters more than the machinery, and the stance has to be right before anything is switched on.

## What hand-written instincts cost

Chapter 19 described how an organisation on The Grove reads its own state. Underneath that read sit two kinds of rule.

The first is the organisation's law: who holds which seat, how consent works, who controls which domain, the guardrails, how a proposal becomes structure. The law is code, deterministic and readable, and it should stay that way. Self-management depends on everyone being able to see why something happened.

The second kind is closer to instinct. Where a piece of work is first sent. When work passed back and forth counts as a bounce. When a branch has drifted from its purpose. When a branch looks ready to divide. Today those are rules we wrote by hand, with thresholds we chose, and they're our best guesses. That has a cost. Code can only cover what its authors thought might happen. A rule tuned on one kind of organisation reads every other kind through the same lens: a bakery and a clinic get the same idea of what strain looks like. And when an organisation does something nobody anticipated, a hand-written rule either misses it or misreads it.

## A body that can feel its insides

There's a word in physiology for the sense a body has of its own condition: interoception.[^1] Hunger, strain, ease, the racing heart before you've named the fear. It's not one of the five senses we learn about at school, and it's arguably the one a living thing can least do without. A vehicle doesn't need it. A pilot reads dials. A living thing has to feel its own insides, or it can't look after itself.

An organisation run as a vehicle has dashboards and pilots. An organisation that's alive in the sense Chapter 5 described needs something more like interoception: a felt sense of where it's strained, what it's missing, where something wants to move.

> *An organisation isn't a vehicle with pilots sitting in separate cabins. It's closer to a living thing, and a living thing knows how it is from the inside. That's what I want for the organisations on The Grove: not more dials, but a sense of themselves that everyone in them can feel and answer to. Collective intelligence isn't in any one person, or in a machine. It's in the loop between them.*

What we're building towards, and calling for now the organisation's nervous system, is a small learned model that grows those instincts from what organisations actually do, so the organisation can feel its own state. Wise-Eye, the large model from Chapter 22, stays the voice. The nervous system senses. Wise-Eye puts it into words.

## How it's meant to work

There are four parts, and only one of them is learned by us.

**A borrowed sense of meaning.** A small, ready-made model turns any piece of text, a purpose, an accountability, a piece of work, into a point in a space of meaning, so "an invoice from the mill" sits near "paying suppliers". It doesn't talk or reason. It just places things near what they're like. We don't train it.

**Memory.** For anything new, the organisation's own most similar past cases, and what became of them. This is how an organisation can know itself without a model of its own: the last time work like this arrived, it went there, and it stayed.

**The learned instinct.** A small model trained on how organisations move, day by day: their whole shape, the work flowing through, their bets and proposals, who holds what by number and never by name, and what followed. Small enough to run cheaply, and in time to run inside the organisation's own space.

**The voice.** Wise-Eye, called when something needs explaining to a person.

If you want an analogy, Daniel Kahneman's two speeds of thinking is a fair one: something fast and wordless that notices, beside something slower that can explain.[^2] The analogy only goes so far. Here the fast part never decides anything, and neither does the slow one.

## What it might sense, in time

These are possibilities, framed as the organisation reflecting back to itself, never as alerts:

- Work that keeps arriving with no good home: a branch or an accountability wanting to exist.
- Strain before it breaks: a branch looking the way branches often look a few weeks before they divide.
- Drift: a branch whose purpose says one thing while its work says another.
- A proposal's consequences before it's decided: about a third of the week's work would land here.
- Power or budget gathering quietly in fewer hands, shown as shape.
- How well the organisation follows when the work the world sends it shifts.
- The softer signals: themes rising across the Field before anyone names them, the Clearing thinning across the whole after a hard decision (the total only, never who came), bets quietly abandoned, the same tension raised again and again.
- Across the network: organisations whose shapes complement each other, and starter packs grown from the patterns of organisations that flourished from a similar start.

## Where it stops

Every part of the stance is a design decision, and each has a reason.

**It senses; the law acts.** Nothing it says changes the organisation except through the same rules as anything else: a person raises a proposal, a forum consents. A model's view must never become an unaccountable power. This is the same firewall Chapter 19 described, carried forward.

**Never the average.** A model trained to copy what's typical pulls every organisation towards the typical, and that's a quiet boss. So it's trained towards outcomes, and learns most from organisations that did unusually well under the same constraints. The operating system exists so organisations can become themselves, not each other.

**Where it hasn't been, it goes quiet.** When an organisation goes somewhere the model hasn't seen, it says it doesn't know and defers to the people. That's exactly where self-managing organisations invent, and the last thing they need there is a machine's guess dressed as knowledge.

**Consequence, not verdict.** For a proposal it shows what would follow, never a score that sways consent. That fits Chapter 11, where there's no override, and Chapter 29, where simulation is for rehearsing, not foretelling.

**Shape, never a judgement of a person.** It can name what's already public, who holds which seats, where the budget sits, and point at gaps in how things are checked, like money resting on one person's word. It never says what someone intends. It never moves anyone's reputation. A suspicion goes to people, through the trust and conflict process in Chapter 12, with the person present.

**Open to everyone.** Any member can ask about the whole. No seat holds a privileged view. Deborah Gordon's harvester ants, from Chapter 4, are a fair picture of why: the colony's intelligence lives in its trails, not in any ant, and the trails are there for every ant to follow.[^3] Each branch also gets its own neighbourhood, read close, so the people nearest a part can see it best. But nobody gets a view the others can't have.

**Learning together, without collecting anyone's data.** One shared base model, with each organisation's own records sitting beside it as memory. Organisations keep their records. When the network learns, it learns from changes to the model sent back, not from records handed over, a method known as federated learning.[^4] That fits the design in Chapter 27, where each organisation is its own DAO and carries everything it needs.

**Memory every night, learning every month, and only after a check.** The organisation's own day goes into its memory nightly. The shared model is retrained from time to time, runs in the shadow of the old one, and replaces it only when it does better on organisations it hasn't seen.

## The loop that closes

None of this is collective intelligence on its own. A model that senses and reports into a void is just another dashboard. The intelligence, if it comes, lives in the loop: the organisation reflects back how it is, people respond where they stand, and the next reflection carries what they did. Nobody can hold the whole of an organisation in their head. But anyone can ask it how it is.

Stafford Beer, whose viable system model runs through Chapter 20, built that model on the human nervous system.[^5] What he couldn't do in the 1970s was give an organisation's sense of itself to everyone in it at once. That's the part we're reaching for.

## Talking to it, and a level up

Because Wise-Eye is its voice, the sense of itself isn't only something to look at. It's something to ask. How are we doing? Where are we strained? What are we missing? Any member could put those questions to the whole and get an answer in plain words, with the reading behind it, and with "we don't know" where the model hasn't been.

The same pattern could repeat a level up. Each organisation on The Grove is a part of a network, and the network learns from changes to the model sent back, never from records handed over. Read in the same way, the network could reflect back its own state: needs that no organisation is meeting, organisations whose work complements each other's, strain rising across many at once, a shift in the work the world is sending. Chapter 2 called society an intelligence with no one home, acting on us unseen. A network of organisations that each sense themselves could give us the first read back from a piece of it.

This is the furthest out of anything in this chapter. Nothing about it is designed beyond the idea, and the same stance would hold: it senses and never acts, it shows shape and never people, and it's open to everyone.

## How we decided

We kept the law and the instinct apart because they fail differently. A law people can't read is a boss. An instinct that's only a guess is a blind spot. Learning the instinct while keeping the law readable lets each be what it's good at.

A handful of early experiments, on simulated organisations only, shaped the stance. Each is here because it changed a decision, not as a result.

A small model learned, from shape alone, when a branch was ready to divide, closely enough to anticipate nine in ten of Wise-Eye's own offers to split one without ever seeing them. But what it had learned was our own rule read back, not anything people do: where simulated people chose for themselves, the skill didn't carry over. So the instincts have to be learned from behaviour, in volume, and checked against people, never assumed from the code.

A free, ready-made sense of meaning, paired with an organisation's own memory, placed work far more accurately than meaning alone, and was most often right when it was most sure. So an organisation can have a useful instinct from its first weeks, before any model has been trained on it.

A raw model will say it's certain about something people later decided against. So before anything is shown to anyone, its confidence has to be corrected until seventy per cent means right about seven times in ten.[^6]

We also chose not to call what it says a prediction. It's a reading of how things are and what tends to follow, offered for people to think with.

## What we don't know

Whether it can sense an organisation's health from shape alone, we don't know. So far it hasn't sensed power gathering, money going missing or people leaving any better than a guess based on what happened last time. Part of the reason was that the record didn't yet say who holds what; it does now.

Simulated people are models of people. The instincts that matter will only come from real ones, in the sandpit first and then in live organisations, and those will be scarce for a while.

It may never sense some of the things people care about most.

A reading open to everyone could still become something people defer to rather than something they think with. The design leans against that, with consequence instead of verdict, silence where it hasn't been, and people deciding, but only use will show.

And who trains a sovereign organisation's model, on whose machine, and whether the network's shared model is the Steward's to keep, are open questions.

## What you might take from this

An organisation can't look after what it can't feel. Most try to feel through dashboards and through watching people, and both make someone the boss of the reading. A sense of itself that belongs to everyone, that says what it notices and goes quiet where it doesn't know, and that never acts except through people, might let an organisation feel its own insides without anyone standing over it.

Sense in the open; let people act.

---

## Notes and further reading

[^1]: Craig, A. D. (2002), "How do you feel? Interoception: the sense of the physiological condition of the body", *Nature Reviews Neuroscience*, 3(8), 655 to 666.
[^2]: Kahneman, D. (2011), *Thinking, Fast and Slow*, Farrar, Straus and Giroux.
[^3]: Gordon, D. M. (2010), *Ant Encounters: Interaction Networks and Colony Behavior*, Princeton University Press.
[^4]: McMahan, H. B., Moore, E., Ramage, D., Hampson, S. and Agüera y Arcas, B. (2017), "Communication-Efficient Learning of Deep Networks from Decentralized Data", *Proceedings of the 20th International Conference on Artificial Intelligence and Statistics*.
[^5]: Beer, S. (1972), *Brain of the Firm*, Allen Lane. For the model put to work in companies, and its debt to neurology: Pfiffner, M. (2022), *The Neurology of Business: Implementing the Viable System Model*, Springer.
[^6]: On why modern models are overconfident, and how their confidence is corrected: Guo, C., Pleiss, G., Sun, Y. and Weinberger, K. Q. (2017), "On Calibration of Modern Neural Networks", *Proceedings of the 34th International Conference on Machine Learning*.
