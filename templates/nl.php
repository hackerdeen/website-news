{% extends "page.php" %}

{% block title %}{{ letter.title }}{% endblock %}

{% block page %}
<h2>{{ letter.title }}</h2>
{{ letter.body|safe }}
{% for article in letter.articles %}
<p><a href="{{ article.file_base }}.php">{{ article.title }}</a></p>
{% endfor %}
{{ letter.footer|safe }}
{% endblock %}
