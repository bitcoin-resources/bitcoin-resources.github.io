---
layout: resources
title: New Book Site
image: /assets/images/bitcoin-resources-twitter-cover.png
description: Curated Bitcoin books.
---

{% assign sorted_categories = site.categories | sort: 'order' %}

{% for cat in sorted_categories %}

## {{ cat.title }}

{% capture my_include %}{% include category-{{ cat.short }}.md %}{% endcapture %}
{{ my_include | markdownify }}

{% include books.html category=cat.short above_the_fold=true %}

[View all books in {{ cat.title }} »]({{ cat.url }})

{% endfor %}

---

[« back to overview][index]

[index]: {{ '/books' | absolute_url }}

{% include bibliography.md %}
