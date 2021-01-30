---
layout: resources
title: Bitcoin Books
image: /assets/images/bitcoin-resources-twitter-cover.png
description: Curated Bitcoin books.
---

# Bitcoin Books

Thanks to Bitcoin, my list of books to read gets longer and longer, way quicker
than I could ever read them. The books listed below are books I can personally
recommend. If a particular book is not listed here, it is probably because I
didn't get around to read it yet. Although there is some overlap, the books are
roughly grouped by topics as follows:

- [Bitcoin (non-technical)][bitcoin-non-technical]
- [Bitcoin (technical)][bitcoin-technical]
- [Economics][economics]
- [Money][money]
- [Banking][banking]
- [The Big Picture][the-big-picture]
- [Software and Programming][software-and-programming]
- [Computation and Complexity Theory][computation-and-complexity-theory]
- [Nassim Taleb (Incerto Series)][nassim-taleb]
- [Work][work]

[bitcoin-non-technical]: #bitcoin-non-technical
[bitcoin-technical]: #bitcoin-technical
[economics]: #economics
[money]: #money
[banking]: #banking
[the-big-picture]: #the-big-picture
[software-and-programming]: #software-and-programming
[computation-and-complexity-theory]: #computation-and-complexity-theory
[nassim-taleb]: #nassim-taleb
[work]: #work

I hope to update this list continually as my reading progresses.

Some of the books listed below were discussed at the [Bitcoiner Book
Club](https://www.youtube.com/playlist?list=PL8GxRkxnvMl3_O3DYNQJFnVBvvt8A9qqW)
organized by John Vallis.

---

<center>
  <p><small><a href="#toc">↓ Table of Contents ↓</a></small></p>
</center>

---

## Bitcoin (non-technical)

Books about Bitcoin which can be read by anyone, no special background knowledge
or education required. As mentioned above, I consider [The Bitcoin
Standard][the-bitcoin-standard] required reading for anyone interested in
Bitcoin.

{% include books.html category='non-technical' %}

Even though [Bitcoin Money][bitcoin-money] is a children's book, it drives home
the value proposition of Bitcoin in a succinct way, making it valuable for
readers of all ages.

{% include books.html category='non-technical2' %}

More books are coming out every year, relating Bitcoin to different fields
and examining it from different angles.

{% include books.html category='non-technical3' %}

The Internet of Money books are a collection of talks by Andreas Antonopoulos,
most of which are available for [free on YouTube][aantonop-bitcoin-talks]. The
Book Of Satoshi is a collection of Satoshi Nakamoto's writings, which are
available for free at the [Satoshi Nakamoto Institute][complete-satoshi].

{% include books.html category='non-technical4' %}

[bitcoin-money]: {{ '/books/bitcoin-money' | absolute_url }}
[aantonop-bitcoin-talks]: https://www.youtube.com/playlist?list=PLPQwGV1aLnTthcG265_FYSaV24hFScvC0
[complete-satoshi]: https://satoshi.nakamotoinstitute.org/

## Bitcoin (technical)

If you would like to dig deeper or get your hands dirty with programming, these
books are for you. Technical knowledge and skills in computer science,
programming, and/or mathematics are beneficial.

{% include books.html category='technical' %}

Mastering Bitcoin is [available for free on GitHub][mastering-bitcoin-free].
Programming Bitcoin includes plenty of [programming
exercises][programming-bitcoin-exercises], which are available for free on
GitHub as well. Grokking Bitcoin is [available for free on
GitHub][grokking-bitcoin-free] as well.

[mastering-bitcoin-free]: https://github.com/bitcoinbook/bitcoinbook
[programming-bitcoin-exercises]: https://github.com/jimmysong/programmingbitcoin
[grokking-bitcoin-free]: https://github.com/kallerosenbaum/grokkingbitcoin
[wikis-and-guides]: #wikis-and-guides

## Economics

Bitcoin is capable of being the new base layer of our economy, which is why
understanding economics is essential in understanding Bitcoin. Bitcoin's
monetary policy is aligned with the Austrian School of economic thought, which
is why reading the works of Austrian's such as Hayek, Hazlitt, Hoppe, Menger,
Mises, Rothbard (and others) is recommended by those who take Bitcoin's value
proposition seriously.

{% include books.html category='economics' %}

Human Action, Mises' magnum opus, is [freely available][human-action-free] as
both an ebook and an audiobook.

[human-action-free]: https://mises.org/library/human-action-0

## Money

In stark contrast to our current economic system, Bitcoin does not offer the
possibility of inflating the monetary base. Understanding money - and especially
*sound* money - is paramount to understanding the value proposition and ultimate
impact of Bitcoin.

{% include books.html category='money' %}

All of the above are available for free at the Mises Institute.

## Banking

Banking is a mystery to most, and central banking doubly so. Bitcoin isn't
necessarily an enemy of the former, but, if successful, it will abolish and
replace the latter.

{% include books.html category='banking' %}

## The Big Picture

Bitcoin is an empowering, freedom-enabling technology. It allows individuals to
become self-sovereign in matters of money and finance, just like other
information technologies enable self-sovereignty in matters of information and
communication. What this implies, and how the world might change because of it,
is the scope of [The Sovereign Individual].

{% include books.html category='macro' %}

We are currently living through the fourth great shift, moving from an
industrial to an information-based society. There is no better book to
understand this shift than the one by Davidson and Rees-Mogg.


[The Sovereign Individual]: {{ '/books/the-sovereign-individual' | absolute_url }}

## Software and Programming

Bitcoin is free, libre open-source software. It is free as in freedom, free as
in free speech. What this means, why free software exists, and what the
implications of free (vs proprietary) software are, is important to understand
the unstoppability of Bitcoin. I would argue that the ethos of GNU and UNIX
programming are important cornerstones for Bitcoin as well.

{% include books.html category='software' %}

## Computation and Complexity Theory

While Bitcoin is in the business of verification and not computation, knowing
the limits of what computers can do and what future computers might be able to
do can be beneficial to better understand some parts of Bitcoin. I highly
recommend [Gödel, Escher, Bach][gödel-escher-bach] because it is a deeply
fascinating and beautiful book.

[gödel-escher-bach]: {{ '/books/gödel-escher-bach' | absolute_url }}

{% include books.html category='computation' %}

[Quantum Computing Since Democritus][quantum-computing-since-democritus] is
quite dense, but it is also quite entertaining at times. The [lecture
notes][quantum-computing-since-democritus-free] which this book is based upon
are freely available online. Note that the first couple of chapters stay in the
non-quantum world of computing and might help to understand why breaking
Bitcoin's security is so hard. [A New Kind of Science][a-new-kind-of-science] is
certainly not for everyone, but it beautifully shows how simple rules can lead
to complex systems.

[quantum-computing-since-democritus]: {{ '/books/quantum-computing-since-democritus' | absolute_url }}
[quantum-computing-since-democritus-free]: https://www.scottaaronson.com/democritus/
[a-new-kind-of-science]: {{ '/books/a-new-kind-of-science' | absolute_url }}

## Nassim Taleb

Highly improbable events, such as the invention of Bitcoin, are almost
impossible to predict. However, [Nassim Nicholas Taleb][nntaleb] wrote multiple
books on concepts that help to foster a solid understanding of Bitcoin. In
short, the invention of Bitcoin is a *Black Swan* event resulting in an
*antifragile* organism. Miners are *"fooled by randomness"* to keep it alive,
and participation requires *skin in the game*.

{% include books.html category='taleb' %}

[nntaleb]: https://twitter.com/nntaleb

## Work

Decentralized networks like Bitcoin, and the internet before it, change the way
people interact and work with each other. People who work on or create content
for Bitcoin are located all over the world, thus regular approaches to work
might not produce the best results. I found the following books to hit a certain
nerve, speaking as someone who has stepped outside of the regular way of working
on things. If you think about working on Bitcoin or other open-source projects,
these books are for you.

{% include books.html category='work' %}

---

[« back to overview][index]

[index]: {{ '#books' | absolute_url }}

{% include bibliography.md %}
