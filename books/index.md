---
layout: resources
title: Bitcoin Books
image: /assets/images/bitcoin-resources-twitter-cover.png
description: Curated Bitcoin books.
---

The following is an incomplete list of Bitcoin books worth reading. Some of the
books listed below were discussed at the [Bitcoiner Book
Club](https://www.youtube.com/playlist?list=PL8GxRkxnvMl3_O3DYNQJFnVBvvt8A9qqW)
organized by John Vallis.

Jump to the [table of contents](#toc) to get an overview of the various sections.

---

<center>
  <p><small><a href="#toc">↓ Table of Contents ↓</a></small></p>
</center>

---

{% assign sorted_categories = site.categories | sort: 'order' %}

{% for cat in sorted_categories %}

## {{ cat.title }}

{% capture my_include %}{% include category-{{ cat.short }}.md %}{% endcapture %}
{{ my_include | markdownify }}


{% if cat.short=="non-technical" %}
{% include books.html category=cat.short above_the_fold=1 %}
{% include books.html category=cat.short above_the_fold=2 %}
{% else %}
{% include books.html category=cat.short above_the_fold=true %}
{% endif %}


[View all books in {{ cat.title }} »]({{ cat.url }})

{% endfor %}

---

## List of All Books

For you CTRL+F freaks.

Also make sure to check out [bitcoiner books](https://www.bitcoinerbooks.com/), [JBP's list of great books](https://www.jordanbpeterson.com/great-books/) and [Athena Alpha's list of Books](https://www.athena-alpha.com/books/).

{% include books-list.html %}

[View book wall »][books-wall]

[books-wall]: {{ '/books/wall' | absolute_url }}

---

[« back to overview][index]

[index]: {{ '/books' | absolute_url }}

{% include bibliography.md %}
