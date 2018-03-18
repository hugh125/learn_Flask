# -*- coding: utf-8 -*-
'''
{% extends "base.html" %}
{% block title %}user on this.base{% endblock %}
{% block page_content %}
<div class="page-header">
    <h1>Hello, {{ name }}-on this.base!</h1>
</div>


<form method="post">
    {1{ form.hideen_tag() }}
    {2{ form.name.label }} {{ form.name() }}
    {3{ form.submit }}
</form>

{% endblock %}
'''