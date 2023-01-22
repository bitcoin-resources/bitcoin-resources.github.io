---
layout: resources
title: New Book Site
image: /assets/images/bitcoin-resources-twitter-cover.png
description: Curated Bitcoin books.
---


{% for cat in site.categories %}
## {{ cat.title }}
{% include books.html category=cat.short %}
{% endfor %}

---

[« back to overview][index]

[index]: {{ '/books' | absolute_url }}

{% include bibliography.md %}
