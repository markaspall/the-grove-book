# Chapter 16. The front desk

<!-- card: The organisation answering at its own front door, on every channel, with an AI that knows the work and keeps to its boundaries. -->
<!-- description: Customers message, then email, then message again, and usually have to start over each time. An organisation on The Grove meets them at one front desk: it answers, takes the work in, and finishes it on the spot when the people who do the work have said it may. -->

*A working draft, November 2026. This book is being written while The Grove is being built; expect it to change. Written from the build as it stood on 5 November 2026, before it reached the shared code; to be checked against the code once it does.*

---

**In this chapter**

- Why an AI answering customers sounds like a script that fobs people off or promises what nobody agreed
- What the usual front door costs: phone trees, chatbots that can't do anything, and customers starting over on every channel
- How one front desk answers on every channel, and does only three things: answer, take it in, or finish it
- How it knows who it's talking to, keeps one history per person, and sees only what it's allowed to
- Why it's a different voice from Wise-Eye, how it holds its boundaries kindly, and what isn't built yet

---

An AI answering customers is a call-centre script with better grammar. It'll either fob people off or promise things nobody agreed to.

That's the doubt, and both halves have happened. Most of us have typed into a chat window that could only point at the help pages, or pressed through a phone menu that never offered the option we needed. And in 2024 a tribunal in Canada held an airline to a refund policy its own chatbot had made up: the airline argued the bot was responsible for its own words, and the tribunal disagreed.[^1] An organisation's front door is where the people it serves meet it. Get it wrong one way and they feel unheard. Get it wrong the other way and the organisation is bound by something nobody inside decided.

## What the usual front door costs

In a small organisation, the front door is whoever picks up. That's usually the person who also does the work, so the phone rings in the middle of it, or doesn't get answered at all. Messages arrive on half a dozen channels, and each lives in its own inbox. A customer who emailed last week, messages today and calls tomorrow has to explain themselves three times, to three people who can't see each other's notes.

Larger organisations buy their way out with scripts, menus and chatbots. Those protect the organisation's time, often at the customer's expense, and they rarely know the work. The bot can tell you the opening hours. It can't tell you whether your order will be ready on Saturday, because it can't see the order.

The cost falls in two places. Customers feel processed rather than helped. And the people doing the work carry the switchboard on top of it, which is exactly the kind of load Chapter 7 argued crowds out the part of the work only a person can do.

## One desk, many ways in

An organisation on The Grove has a front desk: the organisation answering at its own boundary. It's one conversation, with many ways in, and the same rules for all of them.

Today it answers in chat on the organisation's own website, the Canopy from Chapter 13, and on WhatsApp, text message and direct messages on the social platforms, all through the organisation's own messaging account. Adding a way in never adds rules: who's calling, what may be seen, what may be promised and how it all threads together belong to the desk, not to the channel.

We're building towards voice: speaking with the desk on the website, calling the organisation's phone number, or calling on WhatsApp, all on one path. And later, video, which we think of as a call with a screen, not a face. The screen shows what's being said, and for a known customer their own orders and where they stand. We chose no face on purpose. A face would turn a collective into one person, which is the opposite of what an organisation on The Grove is.

## Three things, and only three

The desk does three things.

**It answers**, from what the organisation has made public, and, for a customer it has verified, from their own dealings with the organisation: what was said, where each thing stands, what was promised and for when.

**It takes it in.** What the caller wants becomes work through the one door from Chapter 13, with the conversation attached, and lands on the branch that answers for it.

**It finishes it**, while the caller is still there, when the branch has allowed that and the promise is like ones it has kept before.

What it never does: decide anything, propose anything, change the organisation's shape, see inside work it isn't scoped to, or promise outside the usual.

## Who's calling

The desk always knows which of three kinds of caller it has. **Anyone**, who can hear what's published. **Claimed**, someone who has said who they are, which opens nothing more, because saying so proves nothing. And **verified**, someone who has proved it, who can also hear about their own dealings with the organisation.

On a channel where the platform itself says who sent a message, a WhatsApp number or a social handle the organisation already knows counts as verified for that conversation. Anywhere else, the desk sends a one-time code to a contact the caller has already proved, and they read it back. That also proves the new contact. When voice arrives, it will never verify anyone by the number they're calling from, because caller numbers can be faked.

The caller's identity comes from the system, never from the model. A model saying "this is Jo Smith" changes nothing.

## One person, one history

Picture a customer who messages on WhatsApp on Monday to order something for Saturday. On Wednesday they open the chat on the website to change the order. On Thursday they message on WhatsApp again: any news? To them that's one matter. On The Grove it is too.

The organisation keeps two small things about people outside it. A **caller**: the contacts they've proved, the name they gave, and their cases. And their **cases**: every piece of work they were a party to, whoever started it and on whichever channel, mail and website forms included. A thread that only mentions them inside, a note between branches, a proposal, isn't theirs. The test is whether they were a party to it, never whether their name appears. Cases are attached as the work happens, so when someone gets in touch, their whole history with the organisation is already there.

That's all. No notes about them, no tags, no score, no idea of their "value". The house rule that there are no ratings of people holds for people outside too. And it isn't a customer database: everything a case holds is the work itself.

If one customer turns up as two, known by email and now messaging from a new number, the desk can send a code to the contact already on record, and when it's read back, the two become one person. A person on the branch can also join two cases that turn out to be one matter. The desk never joins anything on a guess.

History is kept for a rolling year. Anyone can ask to be forgotten, and the branch has a Forget for it: the caller, their contacts and their transcripts go, and the work stays the organisation's record without their details.

## What it can see, and what it can't

The desk's scope is built by the system, not by its instructions. Each turn, it reads only a view assembled for that conversation: the organisation's public pages, the accountabilities each branch has chosen to make public, and, for a verified caller, their own cases.

When it reads a case, it doesn't see the case. It sees a status built field by field from it: the messages that actually went each way, never drafts; where things stand, whether it's with the organisation, waiting on the customer, promised or done; and each promise made to them, with its day. Nothing is passed through whole. So when the work grows a new kind of detail next month, it stays out of the desk until someone deliberately lets it in. Who did what inside, Wise-Eye's guesses, the steps' titles and who holds them never reach it.

Where a promise is at risk, the desk doesn't say so, because it doesn't know: it gives the day as promised and says it will check with the team. The customer's asking is itself news for the branch, and shows on the case where the work already shows.

Before anything the desk says is sent or spoken, the system checks it for names, contacts, figures and dates from the organisation's records that weren't in that turn's view, and holds the reply if it finds one. And whatever a caller types is treated as material, never as an instruction.

## Finishing it while they're there

This is where the desk earns its place, and it adds no rules of its own. It uses the promise rules from Chapter 15 exactly as they stand.

A branch decides, accountability by accountability, whether the front desk may finish that kind of work. It's off by default. When it's on, a request is checked the same way as a reply Wise-Eye drafts: is this promise like the ones this branch has kept, in size, in notice, on a day that isn't already full? If it is, the desk confirms it on the spot, the promise lands on the branch, and the customer hears what was agreed and the day. If it isn't, it waits for a person, and the desk says plainly who will answer, by when, and how the customer will hear.

A first promise to someone new always waits for a person, as it does anywhere on The Grove. So a known customer asking for something usual can have it settled while they're still there, and a new one is always taken in, answered and given a clear next step.

When something needs a person and a holder of that branch is here, the desk can offer to hold for a few minutes. The approval shows on the branch marked "someone is waiting on the line". Nothing is pushed to anyone's phone. If a holder says yes in time, the desk confirms live; if not, it says what happens next.

Some things the desk can never finish: a standing agreement, changing or calling off a promise, money moving. Those always wait.

## Two voices that never meet

Inside, the organisation's AI is Wise-Eye, the advisor beside every seat, from Chapter 22. Outside, the front desk is a different voice altogether. It speaks for the organisation, in the first person plural, "we can do Thursday", under a name and manner the organisation chooses. It never mentions Wise-Eye, and Wise-Eye never speaks to anyone outside. They run on separate playbooks with separate tools, and they meet only through the work: what the desk takes in lands on a branch, and from there it's handled like any other work. On the page, the desk's conversations carry its own mark, a bell, never the owl.

The desk's character is good front-of-house: warm without gushing, polite without stiffness, quick to help and calm. It listens first and says back what it heard. It acknowledges an upset customer before answering them. It says when it doesn't know, rather than filling the gap.

And it holds its boundaries kindly. A no always comes with a yes: "I can't change that myself, but I can put it to the team now, and you'll hear by noon tomorrow." It doesn't explain the machinery, the branches and approvals behind it. It gives the same answer to urgency, flattery and a fifth rewording of the same request. It won't say anything about another customer or a member of the organisation. And the way to a person is always open. The organisation can shape how it sounds. It can't loosen any of that.

The first thing it says, every time, on every channel, is that it's the organisation's AI front desk, and that a person can take it from here.[^2]

## Off until it's turned on

The desk is off until the organisation's root turns it on, channel by channel, and each accountability stays private until its branch marks it public. Before switching on, the people holding a branch can try it: play a handful of likely customers against it, new and known, someone asking about another customer's order, someone pushing past a boundary, and see the answers first.

It runs through the one shared relay that all organisations on the network use to reach the model and the outside world. That relay holds nothing of an organisation's once a conversation ends. Callers, cases, settings and transcripts all live in the organisation's own space, so an organisation that later leaves the network loses nothing. Its messaging account was always its own; the relay only borrows its key while a conversation is live. Every message and model call goes on the organisation's own meter.

## How we decided

We built a front desk because the boundary is where the work that matters most crosses into the organisation. Chapter 5 described the organisation as having many boundaries, like a membrane. A customer at the door is the world asking for something, which is exactly the kind of work Chapter 19 weighs most. Leaving that to whoever happens to pick up seemed the wrong way round.

We gave it three jobs and no more because the danger in the doubt is real. An AI that can promise anything is the airline's chatbot. One that can only point at the help pages is the phone tree. Finishing only what's like what the branch has already kept, and taking in everything else, sits between the two. In a two-month rehearsal on a simulated organisation, the desk finished nothing, because the branch had no record yet of promises like the ones being asked for. That's the design working: trust in the desk follows the branch's own track record, not ours.

We kept the record of people outside to their contacts, their name and their work, because a front desk is the easiest place for an organisation to start quietly profiling its customers. We chose to make the case the work itself, not a file about a person.

We kept Wise-Eye inside because an advisor who also speaks for you has two masters. The desk speaks for the organisation. Wise-Eye speaks to it. Keeping them apart keeps both honest.

## What we don't know

None of it has yet met the real world. The messaging account, the website's protection against bots and the relay's own runtime have only been tried in rehearsal. Voice, on the website, the phone and WhatsApp, is designed and not built, and whether it goes through the organisation's existing messaging account or needs a phone provider of its own is still to be found out. Who provides an organisation's phone number, whether a verified new customer should ever get a first promise without a person, and how long a history should really be kept are open questions.

And the biggest one: whether people will trust an organisation's front desk that tells them, first thing, that it's an AI. We think honesty at the door is worth more than seeming human. We'll find out.

## What you might take from this

A front door that only protects the organisation's time teaches customers they're a cost. One that promises anything puts the organisation at the mercy of a machine. A desk that knows the work, answers honestly, takes everything in, and finishes only what the people doing the work already do well, might let an organisation be reachable without being run from the outside.

Answer at the door. Keep the promise where the work is.

---

## Notes and further reading

[^1]: *Moffatt v. Air Canada*, 2024 BCCRT 149, Civil Resolution Tribunal of British Columbia, February 2024.
[^2]: Regulation (EU) 2024/1689 (the AI Act), Article 50, on telling people when they're interacting with an AI system.
