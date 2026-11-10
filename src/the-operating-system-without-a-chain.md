# The operating system without a chain: a peer-to-peer concept

<!-- card: What if the operating system ran on people's own phones, laptops and a pool of servers, with no blockchain underneath? A concept, shared for your feedback. -->
<!-- description: A concept, not a plan: the operating system running peer to peer across phones, desktops and a pool of servers, with no blockchain and no permanent centre. What it would take, what a network would gain and lose, and the questions we'd most like help with. -->

*A concept, November 2026. Not a plan and not built. Shared in the open, for feedback.*

---

**In this chapter**

- Why we're asking whether the operating system could run with no blockchain underneath it
- How an organisation's truth could live on its people's own devices
- How a pool of servers keeps everyone alive and meets the outside world, without becoming a centre
- What a small kernel is, and how a new one would go live with every organisation able to see it first
- What a network would gain and give up, and the questions we'd most like answered

---

Everything before this chapter describes the operating system on the Internet Computer. Chapter 6 gives the reasons, and they still stand: no single point of control, software that can be changed only by those who control it, and independence all the way through. That's the road we're on.

This chapter looks down a different road. It's one we've been thinking about, and we'd rather think about it in the open than in private.

The question is simple. Every organisation running on the operating system is meant to depend on nothing that can be taken away or used as leverage. But a blockchain platform is something an organisation depends on too. It's a far better dependency than a company's servers: no one party can switch it off or change the terms. Still, it's there, and it's permanent. So we asked what it would take to remove any permanent central component at all, and run the operating system through the apps people already carry: their phones, their laptops, and some servers.

It's a concept, worked through in one long conversation. Nothing here is built, and nothing here is decided. We're sharing it because we'd like to know where it breaks.

## One caution first

It would be easy to read this as "the blockchain was the weak point". It isn't. Today the weaker points sit beside it: the shared service that carries messages between organisations and the outside world, and the single key used to call the AI models. This concept moves both of those onto servers a network runs for itself. It doesn't make them go away.

So the case for it doesn't rest on decentralisation as such. It rests on three things: working when offline, keeping readable data off anyone else's machines, and a network owning the ground it stands on.

## The shape

One app runs everywhere, with different jobs switched on depending on the device.

- **Phones** are light members. They hold a recent, partial copy of the organisations their person belongs to. They sign and check what happens, work offline, and catch up when they're opened. They can't stay awake in the background, so they can't do anything that needs to be always on.
- **Desktops**, on Windows and Mac, are full members. They hold their organisations' whole records and help carry the rest of the network while they're switched on.
- **Servers** are the same app with no screen, in the cloud, in several places. They're always awake.
- **The network** is the boundary. Every device and server on a network helps carry every organisation on it. Networks share nothing with each other, as they don't now.

That last point matters most. People are members of organisations, but devices are members of the network. So a founder working alone, with one phone in their pocket, isn't a lone node that disappears when the phone sleeps. Their organisation is carried by the whole network.

## Truth without a chain

A blockchain solves a hard problem: agreeing on what happened among strangers who don't trust each other. An organisation isn't a crowd of strangers. It's a known group of people, so it needs something lighter.

Each organisation's truth would be its record: a chain of signed events, each naming the ones that came before it. The deterministic core the operating system already has would read that record from the start and arrive at the organisation's state now. Every device checks every event against the rules and ignores any that break them, so a tampered copy of the app can't break the rules for anyone else.

Events come in two kinds.

**Most events merge freely.** Work, documents, threads, sensings and commends give the same result whatever order they arrive in. Two people editing while offline isn't a crisis. Where something really does clash, it isn't quietly settled by the software; it shows up as a tension for people to answer.

**A few need to be final.** Who belongs, who holds a seat, what was decided, money, and promises made to people outside. These are final only at a checkpoint, signed by enough of the organisation's seated members and witnessed by the network's servers.

Here the operating system already has most of what's needed. Its way of deciding, from raising a proposal to the waiting period on high-impact changes, is already a way of agreeing at human speed. The waiting period would double as the time devices have to catch up. Governance would do the job a chain's consensus does now.

**Time belongs to the network.** No device's clock can be trusted, so the order of events comes from what caused what, never from timestamps. Deadlines, the fading of trust and the waiting periods count in the network's witnessed checkpoints. A vote counts only if it lands before the checkpoint that closes its window, so nobody can backdate one.

A device that's been offline for three weeks comes back and its freely merging events join the record. Any final kind it made in the meantime are turned away if the organisation has moved on, and its person is told why.

## The pool of servers

Servers do two kinds of work, and the difference decides who may do it.

**Blind work** can be done by any server for any organisation: storing records that are encrypted so the server can't read them, passing messages between devices, witnessing the order of events, and routing what comes in from outside.

**Sighted work** is only for servers an organisation has chosen as its hosts: running the front desk and the agents, holding the keys to its outside accounts, and calling the AI models. A sighted host can read what it serves, so choosing one is an act of trust.

At first the steward runs the servers, and a founder starts on the steward's host by default. The servers matter most while a network is small, for the times when no desktop is awake. As more organisations join, they'd be asked to host servers for the network, not just for themselves, so the pool grows beyond the steward. Hosting is witnessed, so it can count as a contribution or be a service the hosting organisation charges for.

Is the steward running the early servers a capture risk? For the truth, no. Its servers can't read an organisation's content, and they can't forge a decision, because decisions need members' signatures. What they can do is delay or drop traffic, and see whatever they host as sighted work. The answer to both is the same as everywhere else in this book: every organisation's devices hold its whole record, so it can move to another host and carry on.

## Meeting the outside world

The outside world isn't peer to peer. WhatsApp, email, phone networks and browsers deliver only to a fixed public name. A laptop asleep on home broadband can't answer a customer. So this is where servers stay, however large the network grows.

Each organisation would own its own domain, the same as any business does, and hand part of it to the pool. The pool's servers keep a record of which server is hosting each organisation's front desk at any moment, and answer from it. If that host fails, another takes over in seconds, and the public name doesn't change. There's no central naming service of the network's own.

A founder with no domain on their first day borrows a name, from the steward or from any organisation offering them, and leaves by pointing their own domain at the pool. The same goes for phone numbers and messaging accounts: whoever holds them with the carrier or with Meta holds the door, so an organisation is only truly independent when it holds its own. Borrowed ones are a convenience, with the way out built in from the start.

A few details keep it honest. Only one host runs an organisation's front desk at a time, with a second ready, or two servers would answer the same customer. Everything sent out carries a once-only mark, so nothing goes twice. And if no host is up at all, messages wait in the pool and the front desk falls back to taking a message.

Some central systems can't be designed away: those who register domains, those who issue the certificates that make websites trusted, app stores, phone networks, Meta. The aim isn't to pretend otherwise. It's that none of them is held by the network on everyone's behalf. Each organisation holds its own.

**If an app store ever removed the app,** an organisation's host could still serve the panels as a web page at the organisation's own address, as a canister can. A browser becomes a light member. That's also the way in for anyone who'd rather not install anything in their first hour.

## Keys and secrets

People would hold their own keys, on their own devices, in place of today's sign-in. Phones keep theirs in secure hardware, behind a fingerprint or a face. A lost phone is replaced by seated members countersigning the person's new key. A steward working alone would need named people to recover with, or a lost phone could mean a lost organisation.

Some things get stronger. The front desk would hold only the part of the record it's allowed to use, which is a firmer limit than a rule in code. Some things get weaker. On the Internet Computer, the keys to an organisation's outside accounts can be guarded by many machines together, so that no single machine ever holds one. Here they'd sit on the organisation's chosen hosts, in usable form. The same goes for access to the source code, which is granted by holding an accountability in the steward's branch for the code and never seen by any person. Here the pool would have to guard it the way the Internet Computer can. That's the hardest piece of what the Internet Computer does to rebuild.

And one thing changes shape. The source code can still be sealed. But the compiled app would sit on every phone, laptop and server, where anyone determined enough could copy it, study it and run a changed copy. They still couldn't break the rules for anyone else, because every device checks every event. But the running program would no longer be private.

## A small kernel

If every device checks every event, every device must agree on the rules. That sounds like every organisation having to run the same release, all the time. It needn't.

The test for what has to be the same everywhere is one question: **would two honest devices disagree about the record if they differed on this?** If yes, it belongs in the kernel. If no, it can differ freely.

- **The kernel** holds the shape of an event and its signatures, the ordering, the checkpoints, who belongs and who holds a seat, the guardrails that can't be voted away, and the engine that reads an organisation's own rules. Every device and server on a network runs the same one.
- **An organisation's rules**, every setting it has chosen, its branches and its agreements, are held as data. They change by the organisation's own proposals, with no release involved.
- **Everything else**, the panels, Wise-Eye, the front desk, the connections to outside tools, packs and the nervous system, changes freely, release by release.

The kernel stays small by keeping mechanisms in it and values out of it. We'd expect it to move a good deal at first, while the ways trust, decisions and money work are still being tuned, and then to settle. The long-term risk is creep: every feature someone wants every device to enforce pulls towards the kernel. The test needs a guardian.

One principle in this book would change. Today nobody can push code into an organisation; it adopts a release by its own proposal. Here, taking a new kernel would be a condition of staying on the network. The organisation would still choose: upgrade, or leave.

## How a new kernel would go live

That makes the moment a new kernel goes live the most important decision a network makes. We'd want every organisation to see it working on its own record before agreeing, without anyone outside the branch that holds the code seeing the source.

1. The branch responsible for the code builds a candidate. The full test pipeline runs, and its results are published to the network.
2. A rehearsal network starts on the candidate, cut off from the outside world.
3. Each organisation's devices replay its own record under the candidate and report whether it passes. An organisation that wants more can copy itself into the rehearsal network and work in it for a while.
4. The steward raises the release as a proposal, with the test results and the replay reports attached.
5. The network decides, organisation by organisation.
6. The new kernel takes effect at a named checkpoint. Devices that haven't upgraded can still read, but can't act, until they do.

Step five is a proposal process of its own, run across the network, and it exists for kernel releases and nothing else. It's the same way of deciding organisations already use, one level up, with organisations taking part instead of people. Only the steward raises one. Each organisation gives one signal, signed by its own forum, so size buys no more say than money does. A signal counts only from an organisation with some witnessed history, so nobody can create organisations to swing a release. It passes the way proposals already do, and an objection that can't be resolved goes to a jury. It can never reach inside an organisation. It decides which kernel the network runs, and that's all.

Everything else this concept leaves without a home, the steward settles. Closing the gaps is what it's for. The one decision it doesn't make alone is a new kernel.

## The legal body

Any organisation running on the operating system can take a legal form, as Chapter 18 describes, and a DAO company is the natural one. Would a peer-to-peer organisation still count?

As far as we can tell, nobody approves a DAO in advance. In the law of Wyoming and the Marshall Islands, it's a company that says it is one and points at the code that runs it. Wyoming's articles must carry "a publicly available identifier of any smart contract directly used to manage, facilitate or operate the DAO".[^1] The Marshall Islands asks a DAO to say whether it's managed by its members or by its code.[^2] In what we've read, neither asks for the code itself to be public, or says the code has to run on a public blockchain. An organisation here could point at its address on the network's shared record. It could also publish a fingerprint of its record to a public chain from time to time, giving it a public marker without living there.

We're not lawyers, and this is the part we'd most like someone qualified to read. Member management fits the operating system's design, where people govern and the code is the means. Whether a private network of this kind satisfies the people who keep the registers is a question for them.

## What a network would gain, and what it would give up

A network running this way would gain:

- **No dependence on any platform**, at any level, including the Internet Computer.
- **No fees to run code**, the computing charges every organisation would otherwise pay.
- **Work that carries on offline**, and merges when people reconnect.
- **Readable data on nobody else's machines.**
- **AI that can run locally on a desktop**, including the organisation's own nervous system, which a canister can't do.
- **Dividing an organisation becomes a copy of its record**, each side carrying on from the same history.
- **A network that owns its own ground**, and a new network that starts clean.

It would give up:

- **Agreement, storage and being always on** become ours to build and each network's to run, where the Internet Computer would do them.
- **Someone pays for servers**, the steward first.
- **A sign-in becomes an app to install**, on four kinds of device, with a web page as the way in without one.
- **Keys guarded by many machines together.**
- **A private running program.**
- **Detaching into a network of one gets harder**, because a network of one needs servers of its own.
- **Looking after keys lands on people.**

## What we're least sure of, and where you could help

If you've built peer-to-peer systems, run a co-operative's infrastructure, practised law around DAOs, or simply see a hole, these are the questions we'd most like help with.

1. **Is this worth it?** The trade is a platform every organisation depends on, against a great deal of building for us and running for every network. Does offline work, privacy and owning the ground justify that, or is the Internet Computer the better dependency to have?
2. **Removing someone while they're offline.** A member is removed while their laptop is shut, and goes on working. Removal wins once it's final, but what happens to everything they did in between?
3. **Secrets across many servers.** Is an organisation's chosen host enough, or should every secret be split across several servers so no one machine ever holds it?
4. **Advising without seeing.** People in the network would judge a new kernel by its plain description and by watching it replay their own records, without seeing the source. Is that enough trust?
5. **A security fix.** Debating a hole in the open tells everyone it's there before it's fixed. What's the fast path, and who may use it?
6. **The first hour.** A founder with only a phone starts on a borrowed name, the steward's host and a shared messaging account. Is leaving each of those easy enough, from day one?
7. **The tools.** Holochain, Iroh, Automerge, p2panda, Tauri and the consensus engine CometBFT, which keeps working while fewer than one third of its validators are faulty and lets an application choose who validates,[^3] are among those we'd look at. We haven't assessed any of them for this. Which would you reach for?
8. **The law.** Does a DAO company on a private network meet the Acts as they're applied in practice?
9. **What did we miss?**

The road we're on is the Internet Computer. This is the one we're looking down. If you've walked it, we'd love to hear from you.

---

## Notes and further reading

[^1]: Wyoming Secretary of State, "DAOs: Frequently Asked Questions", citing W.S. 17-31-106(b).
[^2]: Blockworks, "The Marshall Islands Wants Money-making DAOs To Call It Home", on the Decentralized Autonomous Organizations Act of 2022.
[^3]: CometBFT specification, docs.cosmos.network.
