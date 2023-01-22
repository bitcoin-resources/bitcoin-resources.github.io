---
layout: resources
title: Bitcoin Book Wall
image: /assets/images/bitcoin-resources-twitter-cover.png
description: Curated Bitcoin books.
---


{% for cat in site.categories %}

## {{ cat }} {{ cat.name }}

{{ cat.text }}

{% include books.html category=cat.short %}

{% endfor %}

{% include books.html %}

---

[« back to overview][index]

[index]: {{ '/books' | absolute_url }}

{% include bibliography.md %}
