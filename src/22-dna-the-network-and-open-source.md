# Chapter 22. DNA, the network, and why not open source

*A working draft, November 2026. This book is being written while The Grove is being built; expect it to change. Checked against the build as it stood on 1 November 2026.*

---

If you write code for a living, this is probably the question you've been holding since Chapter 5.

You say nobody should be the boss. You say an organisation should be able to leave. You say the system should be impossible to capture. Then open source it. Put the code where anyone can read it, copy it and run it, and the promises keep themselves. Anything less is a company asking to be trusted while it keeps the keys. We've all seen that film. The platform is friendly while it grows, and then the prices rise, the terms change, and the exit turns out to be a door painted on a wall.

It's a fair doubt, and we want to answer it properly. That starts with saying plainly where things stand.

Today, every organisation on The Grove lives in one shared space on the Internet Computer, and we control it. The code is in a private repository that we alone can change. When we release a new version, we install it, and every organisation runs it the next minute. Each organisation's records are kept apart from every other's, and an upgrade carries them over without losing anything, but no organisation chooses whether to take it. The services that set an organisation's plan and decide which AI model does which kind of work run in a separate space that we also control. Nothing described later in this chapter as carried, sealed or chosen exists yet.

We built it in that order on purpose. A network of organisations that can't yet run themselves would be worth nothing, and nobody would want to leave with it or fight to capture it. So we built the organisation first. What follows is the design for the rest, which we've decided and haven't built, and the reasons it isn't simply open source.

## What both answers cost

Most software for organisations is closed and rented. You don't hold it; you visit it. Your records, your history and the way your work is done live on someone else's machine, under terms they can change. Leaving means exporting what they let you export and rebuilding the rest. For an organisation trying to work without a boss, that's an odd place to live. It has removed the boss from inside and accepted a landlord outside.

Open source answers part of that, and the part it answers is real. Eric Raymond's argument from the late 1990s still holds: when many people can read the code, problems surface faster and improvements come from places no single company would think to look.[^1] Code anyone can read is code whose promises anyone can check.

But open source has costs of its own, and the people who know it best are the ones who talk about them most. Nadia Eghbal's study of how open projects are actually maintained found that most rest on a handful of tired people, carrying work that thousands depend on and almost nobody pays for.[^2] Code that's free to copy isn't free to keep. And open code has repeatedly been taken by companies with more money than its makers, run as a service and sold back to the people who wrote it, with little returned.

There's a deeper problem, and it's the one that matters most here. Open source frees the code. It doesn't free the organisation. If your organisation's records live in a space someone else controls, being able to read the software running there doesn't get you out. You can fork the code. You can't fork your history, your agreements or your people unless they're already yours. What traps an organisation is rarely who can read the source. It's who holds the running thing.

## The turn: what's yours and what's ground

So we started from a different question. Not who can read the code, but who can hold an organisation hostage, and how to arrange things so that nobody can.

The answer begins with a distinction we drew in Chapter 5. What makes an organisation that organisation isn't code. It's data: its purpose, its branches and what each answers for, its agreements, the playbook each piece of work follows, the shapes of the records it keeps, the decisions it has made and the record of how. We call this its DNA. It's written and changed by the people in the organisation, through the organisation's own proposals, and it belongs to them.

That part is built. Every organisation on The Grove holds its own DNA, kept apart from every other's, and when it describes itself in its first hour the result is its own pack, held at the root like its purpose. The code underneath is something else. It's the ground the DNA grows in: the means to run, and the few guardrails every organisation carries. We call the smallest core of it, the part nobody can vote away, the kernel.

Once you see the two apart, the design follows. The DNA has to be the organisation's, fully and always. The ground has to be something nobody can take away, including us.

## What we're building towards

Here is the shape we've decided.

**Every organisation will carry the system.** Each will live in its own space, controlled by its own governance, not by us. Inside it, the organisation will carry everything it needs to keep living: its DNA, its members' records, its documents, and the running system itself. It will also carry a sealed copy of the system's source, its history and its full design. The seal isn't held by us. It's a tiny companion space with no controller at all, which nobody can change, and which opens only on one condition we come to below. The organisation runs the system. It can't read the source until it has earned it.

That sealed copy matters more than it looks. If an organisation were given the source only when it left, a captured steward could simply refuse to hand it over. So the copy travels from the first day, is refreshed with every release, and is never replaced, only added to. A steward that slipped rubbish into one release would cost an organisation at most that release.

**Nobody can push a change into an organisation.** A new version arrives in the organisation's space, explained in its own terms: what changes for it, which of its own tensions it answers, and whether it touches a guardrail. Taking it is the organisation's own proposal, on the same clocks as any other high-impact change, with a pause in which a concern can stop it. An organisation can wait, skip a release, or go back to any earlier version it has carried. The archive of versions sits where running code can't reach it, and going back doesn't depend on the running code agreeing to its own removal: enough of the organisation's people, signing with their own keys, can do it from outside.

**An organisation can leave with the system.** Once it has built something real, with verified people holding its root and a record of work done over time, it can detach from its network by its own proposal, needing nobody's permission. It keeps everything it carries and goes on living, on a version fixed in time. Before then, its data is still its own and can be taken at any time. What waits is only the running system, so that founding an organisation isn't a free way to walk off with it.

**The source opens when organisations form a network of their own.** Two organisations that have each qualified, governed by different people, can draft a purpose for a new steward together, pass it through each organisation's own governance, and wait out a cooling-off period. Then each one's seal checks the others and opens. From that moment they can read and change the code, and they become a network in their own right. A branch that splits off to become its own organisation takes a copy of the sealed code with it too.

This is what we mean by open to those who have earned it. Not open to anyone with a browser, and not closed to everyone but us. Open, fully, to organisations that have built something and have chosen to look after the system together.

**The steward is an organisation like any other.** A network of organisations that recognise each other needs someone to maintain the code for it. That steward will be an organisation on the same system, bound by the same rules, whose only difference is that it holds the source and ships releases. It earns its keep by being worth staying with. The steward takes no fee from the services organisations provide to each other: what an organisation earns from its services is its own. An organisation pays it one flat plan for maintaining the system, never per person and never per decision, and is free to top up its own computing directly or bring its own key for AI, which keeps the plan honest.

Today the steward isn't that. It's a separate service we run, and while the system is young no plan is charged. Turning it into an organisation with seats, and handing it the code, is the step after organisations can live in their own spaces.

**And if a steward goes bad, the organisations leave together.** Capturing a steward gets you its business and nothing else. No keys to anyone's space, no only copy of anyone's records, no power to push code, no source held hostage, because every organisation already carries it. Bad code goes uninstalled. A price rise ends with organisations that stop paying. Neglect ends with organisations that pair up, open their seals and steward themselves.

What they do with the code after that is up to them. A new network can change anything, including the guardrails we hold most dear. We've accepted that. A system nobody can trap is one we can't control either. What we've designed is that a network which loosens a guardrail has to ship as a different lineage under a different name, so no organisation mistakes it for an update. Whether to make that a hard rule is still open.

## How we decided

We weighed four answers.

Closed and rented was never on the table. It's the landlord we were trying not to become.

Open source, now, was the strongest alternative, and we took its case seriously. Its best arguments are these. Guardrails nobody can read are guardrails you're asked to believe, and Chapter 5 made the point that a promise in words is weaker than one in structure. Openness invites contribution and catches flaws faster. And a project that keeps its code close while talking about freedom looks like every company that later changed its licence.

We said no for now, for three reasons. The first is capture by money. An open kernel can be taken by anyone well funded, stripped of what makes it hard to boss people with, and offered under a similar name to organisations that can't tell the difference, while the steward maintaining the real thing can't pay for its own work. The second is the safety of organisations' rules. The guardrails hold because no one inside an organisation can change them; a copy of the system that quietly drops one is a risk to every organisation that might run it without knowing. The third is the steward problem. Someone has to maintain the code, answer what organisations feel is missing and keep it secure, and Eghbal's tired maintainers are the warning. Open source doesn't remove that job. It only removes the way of paying for it.

We also tried, for a while, a middle answer: source available only to a legitimate fork, released on request. It failed on the obvious test. If the steward itself went bad, the organisations would be asking it for the way out. That was the moment we saw that the design had a hold in it as well as a hole, and that the only fix was for every organisation to carry the way out from the start.

Elinor Ostrom's work on commons helped us see the result as something other than closed.[^3] The commons she studied that lasted for centuries weren't open to everyone. They had clear edges, and the people inside them made their own rules. A bounded commons is a commons. We hold to that, though we know it's the argument a company keeping control would also make.

What we haven't answered yet is real. An organisation can't check sealed code before it unlocks it; published guardrails, their tests and verifiable builds help, but they aren't the same as reading it. Improvements will come more slowly than in an open bazaar, because organisations send tensions, not code. Whether an independent network can offer its changes back, and on what terms, isn't designed. The licence for unlocked source is still with lawyers, and licences that ask those who only take to pay, while those who contribute go free, are one lens we're looking through. The numbers for qualifying aren't set. And until other stewards exist, leaving is possible but costly, so for now a fair price rests mostly on our own integrity, with open books as the check.

Dee Hock, who helped found Visa as an organisation held by its members, spent his later years warning that such networks drift back towards command and control.[^4] Visa became a conventional listed company in 2008. We read that as the strongest argument against us. Our answer is that recentralising is easiest where the centre holds what members need. We're designing a centre that holds nothing members can't leave with. Whether that's enough, we'll only know when someone tries to take it.

## What you might take from this

Open source asks who can read the code. The harder question is who can hold your organisation, and the answer has to be nobody. Keep the organisation's DNA as its own data, let every organisation carry the system sealed inside its own space, let it choose every change, and let it walk away with everything when the network stops serving it.

The code doesn't need to belong to everyone if every organisation carries it and nobody can take it away.

---

## Notes and further reading

[^1]: Raymond, E. S. (1999), *The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary*, O'Reilly.
[^2]: Eghbal, N. (2020), *Working in Public: The Making and Maintenance of Open Source Software*, Stripe Press.
[^3]: Ostrom, E. (1990), *Governing the Commons: The Evolution of Institutions for Collective Action*, Cambridge University Press.
[^4]: Hock, D. (2005), *One from Many: VISA and the Rise of Chaordic Organization*, Berrett-Koehler.

On code as a kind of law, and why who writes it matters: Lessig, L. (1999), *Code and Other Laws of Cyberspace*, Basic Books.
