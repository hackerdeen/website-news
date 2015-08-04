{% extends "page.php" %}

{% block title %}{{ article.title }}{% endblock %}

{% block page %}
<h2>{{ article.title }}</h2>

<p>{{ article.author }}</p>

{{ article.body|safe }}

{% endblock %}