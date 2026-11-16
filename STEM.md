# STEM learning guide — krampus

KRAMPUS is a composition: MellifluousML, Madi, Gamora (with Berzerker AIO), Eve and Lilith assembled into one verified whole.

This guide is for teachers, mentors, club leaders, parents and students who want to
use this repository as a vehicle for real STEM learning — in particular for girls and
other groups still under-represented in computing, engineering and mathematics. It
says what the project actually teaches, how to run a session with it, and what to
remove so that nobody is excluded by accident.

## What this project teaches

**Subject areas**

- software composition
- interface contracts
- verification
- integration testing

**Skills practised**

- defining a contract between components
- testing a composition rather than a unit
- recognising a version skew before it bites

## Prerequisites

Python 3.13. The suite runs in under a second, so the loop of 'change, test, read the failure' is fast enough for a first session.

Nothing else is assumed for the entry-level activity below: no prior programming
experience, no particular hardware, and no home internet connection.

## Six practices this repository is set up to support

These follow the published guidance on gender-equitable STEM education — connect the
work to learners' lives, let them investigate real problems, treat struggle as part of
the work, name and challenge stereotypes, make the work collaborative, and put
learners in front of diverse role models.

1. **Connect it to their lives.** a band, not a soloist: each part is fine alone and the interesting failures only appear together
2. **Let them investigate.** ask the group to break one component's contract and predict which other components notice
3. **Make struggle normal.** Build the session so that the first attempt is *expected*
   to fail. Say out loud that debugging is the subject, not a penalty. Ask "what did
   that error tell you?" before offering the answer.
4. **Challenge the stereotype.** Name who does this work and why it is not a gendered
   skill. Praise the method ("you isolated the variable"), not the person ("you're a
   natural") — the second kind of praise teaches learners that ability is fixed.
5. **Make it social.** each pair owns one component and must negotiate a contract with the pair next to them, in writing
6. **Show diverse role models.** integration and release engineers, and the women who led platform teams through large-scale migrations

## A 90-minute session

1. *(15 min)* Draw the five components and the arrows between them.
2. *(25 min)* Run the suite and read one failure in full.
3. *(35 min)* Change one contract, then find every place that assumed the old one.
4. *(15 min)* Write the contract down so the next person does not have to guess.

## Vocabulary to define before the session

Specialist vocabulary is a hidden entry test if nobody explains it. Define each of
these the first time it appears, in one sentence, in the learners' own words:

1. **composition** — several parts treated as one system.
2. **contract** — what a component promises its neighbours.
3. **version skew** — parts expecting different rules.

## Accessibility

Read [ACCESSIBILITY.md](ACCESSIBILITY.md) before running a session. Two rules matter
most in a mixed-ability room:

- Every activity must be completable with a keyboard alone, with a visible focus ring.
- Every instruction names the control or the heading ("the **Run** button in the
  toolbar"), never a colour or a position.

Pair learners rather than singling anyone out, and always offer a text-only route for
a visual step.

## Contributing as a learner

Small, well-scoped contributions are the point, not a consolation prize:

- Browse issues labelled
  [`good first issue`](https://github.com/myzticalbabe/krampus/labels/good%20first%20issue).
- Read [CONTRIBUTING.md](CONTRIBUTING.md) — it has a section written for first-time
  contributors.
- Ask in [SUPPORT.md](SUPPORT.md) if anything is unclear. Asking is expected here; it
  is not a failure.

## Licence and classroom reuse

Classroom, club and workshop use is welcome. See `LICENSE` for the exact terms, and
check whether your institution requires a separate agreement before redistributing
modified copies.
