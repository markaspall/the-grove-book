# Chapter 5. Why an operating system

*A working draft, November 2026. This book is being written while The Grove is being built; expect it to change.*

---

If you've followed us this far, you might agree with most of it and still have a fair objection.

All of this sounds like culture. Living organisations, sensing and responding, people taking up responsibility rather than having it handed to them: these are questions of how people behave and what they believe. Culture is built through leadership, conversation, trust and time. It isn't something you can install. If anything, the history of organisational change is littered with software that promised to transform how people work and ended up as one more system to log into.

So why build an operating system at all?

## What culture alone costs

We have a lot of respect for culture. But we've also watched what happens to it under pressure.

A team agrees to make decisions together. It works well for a while. Then a deadline lands, someone senior is anxious, and a decision gets made in a corridor. Nobody objects, because it's urgent and it's only this once. Next time it's easier. Within a year the team is deciding things the old way and talking about the new way at offsites.

This isn't a failure of good intentions. It's what happens when the only thing holding a new way of working in place is everyone's goodwill on a bad day. Old habits have generations behind them. New ones have a workshop and a poster.

The practices that went furthest beyond hierarchy knew this, which is why they wrote things down. Holacracy has a constitution, roles written with their purpose and accountabilities, a governance process with its own rules, and meetings with a facilitator and a secretary to keep it all honest.[^1] It's a serious answer to the drift. But it asks a lot of people. Someone has to run the meetings. Someone has to keep the records. Someone has to know the rules well enough to spot when they're being bent. And the record of how the organisation is meant to work usually lives in a separate place from the work itself: a map of the organisation, consulted now and then, while the real work happens in email, chat and spreadsheets.

When people get busy, the map falls out of date, the meetings slip, and the old shape grows back underneath.

## The thing everything else runs on

Think about the computer you use every day. You probably don't think much about its operating system. You open a window, and a programme runs. You save a file, and it's there tomorrow. Two programmes don't overwrite each other's work. One crashing doesn't take the others down. None of that happens because the programmes are well behaved. It happens because the operating system underneath provides the means for them to run, and the rules they have to run within.

That's the kind of thing we set out to build: not another tool that sits on top of an organisation, but the layer underneath that organisations run on. An organisational runtime.

The comparison holds further than you might expect.

The **hardware** is a blockchain, the Internet Computer, where each organisation lives in its own small, self-contained piece of the network that nobody else controls.

The **operating system** provides the means an organisation needs to run: ways to sense what's happening, make decisions, route work to where it belongs, keep promises, handle money, and see itself whole. And it provides the guardrails: the few rules every organisation carries, which stop it drifting back into the old shape when people are tired or under pressure.

The **programmes** are the organisations themselves. Each one runs on the system, in its own space, in its own way.

And each organisation's **files**, the things that make it *that* organisation, are its own: its purpose, its parts, its agreements, its records, the way its work is done. We think of these as the organisation's DNA. They're data, written and changed by the people in the organisation, through the organisation's own processes. The system doesn't decide what shape an organisation should be. It holds whatever shape the organisation chooses, and makes it easy to change.

## Working in it, not on it

There's a difference between a map of an organisation and the place where the organisation actually works.

Most tools for self-management are maps. They record the roles, the circles, the policies. You go there to look things up, and to change the structure in a governance meeting. Then you go back to your email to do the work.

From the start, we wanted the opposite. Work arrives in the organisation and goes straight to the part that answers for it. A proposal to change how things are done is made where the work is happening, by the people doing it. The structure isn't a diagram beside the work; it's the thing the work flows through. So when the structure is wrong, you feel it in the work, and the work itself shows where.

That's the deeper reason for an operating system rather than a tool. A tool is something you pick up and put down. An operating system is where you are.

## Guardrails, not instructions

The guardrails are worth a closer look, because they're the answer to the culture objection.

The legal scholar Lawrence Lessig made an argument in the late 1990s that has only grown more relevant: in the digital world, code regulates behaviour as surely as law does.[^2] The way a system is built makes some things easy, some things hard and some things impossible, whatever anyone intends.

That cuts both ways. Most software for organisations quietly enforces hierarchy: approval chains, managers who can see their reports' work but not the other way round, dashboards built for the top. Nobody voted for any of it. It's just how the tools were built.

So we built the other way. In an organisation on The Grove, a small number of things are simply not possible. Nobody can grant themselves a seat. Money can fund the work but can't buy a say in decisions. Once there's more than one person, no decision about a part of the organisation is made by one person alone. Nobody can quietly change the rules for everyone else. And no reading of the organisation is ever about an individual. These aren't policies that can be bent in a hurry. They're how the system works.

Everything else is left to the organisation. The guardrails are few, on purpose. They mark the edges of the road, not the route.

## Run by its members, like Visa

There's one more question: who runs the system?

If one company owns the platform that organisations run on, that company holds all the power, however good its intentions. It can change the rules, raise the price, or be bought by someone with different intentions. An operating system for organisations without bosses would have quietly put a boss back on top of all of them.

The nearest model we found is an unlikely one: Visa. In the late 1960s, Dee Hock helped turn a struggling credit card programme into an organisation owned and governed by the banks that used it, neither a single company nor a free-for-all, which he later called *chaordic*: a blend of chaos and order.[^3] The network existed because its members ran it together.

The Grove works on a similar idea. Organisations form a network by recognising each other. The network has a steward, which is itself just an organisation like any other, bound by the same rules, whose job is to look after the system's code for the organisations that use it. Every organisation carries the system with it, sealed inside its own space. Nobody can push changes into an organisation; each one decides for itself whether to adopt a new version. And if a steward ever stopped serving its network, the organisations could leave together, take the system with them, and form a network of their own.

How that works in practice, and why it isn't simply open source, is a story for later in the book. For now the point is simple. The system is designed so that capturing it would be worthless.

## How we decided

We didn't start out building an operating system. We started with governance: a way for an organisation to run itself without a boss, expressed in code. Very early, we found that governance alone wasn't enough. An organisation that can make decisions but can't route its work, keep its promises or see its own state isn't much of an organisation. Layer by layer, what began as governance became the whole runtime.

We argued about the word. *Platform* sounded like someone else's property. *Tool* sounded like something you could put down. *App* sounded small. *Operating system* was the only term that captured both halves: the means to run, and the rules to run within. Holacracy's creators had used it too, for a practice written on paper.[^1] We wanted one that actually runs.

We also had to decide how much to build in. It would have been easy to encode a particular way of organising, ours, and make every organisation follow it. We chose not to. The guardrails are the few things we believe must hold for any organisation without a boss to stay that way. Everything else is the organisation's own DNA. The code is only the ground it grows in.

And we chose a blockchain not because it's fashionable but because it answers a specific question: where can an organisation live so that nobody, including us, can switch it off, read its private records or change its rules from outside? On the Internet Computer, each organisation can control its own space. That was the property we needed.

## What you might take from this

Culture matters, but culture alone erodes under pressure. Rules that live in the structure of the system itself don't depend on everyone's goodwill on a bad day.

That's why an operating system: the means to run without a boss, and the few guardrails that stop the boss growing back.

---

## Notes and further reading

[^1]: Robertson, B. J. (2015), *Holacracy: The New Management System for a Rapidly Changing World*, Henry Holt.
[^2]: Lessig, L. (1999), *Code and Other Laws of Cyberspace*, Basic Books.
[^3]: Hock, D. (1999), *Birth of the Chaordic Age*, Berrett-Koehler. See also Hock, D. (2005), *One from Many: VISA and the Rise of Chaordic Organization*, Berrett-Koehler.
