{% extends "page.php" %}

{% block title %}News{% endblock %}

{% block page %}
<h2>News</h2>
{% for nl in news %}
<a href="{{ nl.file_base }}.php"><h3>{{ nl.title }}</h3></a>
{{ nl.body|safe }}
<h4>Articles</h4>
{% for article in nl.articles %}
<p><a href="{{ article.file_base }}.php">{{ article.title }}</a></p>
{% endfor %}
{{ nl.footer|safe }}
{% endfor %}
{% endblock %}