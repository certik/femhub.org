#!/usr/bin/env python

import os
import datetime

from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader('templates'))

news = [
    (datetime.date(2009, 10, 15), 'New home page launched'),
    (datetime.date(2009, 9, 23), 'FEMhub 0.9.7 released'),
    (datetime.date(2009, 7, 30), 'FEMhub 0.9.6 released'),
    (datetime.date(2009, 7, 14), 'FEMhub 0.9.5 released'),
    (datetime.date(2009, 6, 29), 'FEMhub 0.9.4 released'),
    (datetime.date(2009, 6, 28), 'FEMhub 0.9.3 released'),
    (datetime.date(2009, 6, 26), 'FEMhub 0.9.2 released'),
    (datetime.date(2009, 6, 25), 'FEMhub 0.9.1 released'),
    (datetime.date(2009, 5, 18), 'femhub.org page created'),
    (datetime.date(2009, 5, 13), 'FEMhub distribution started'),
]

def do_strftime(value, format='%H:%M %d-%m-%Y'):
    """Format a datetime, date or time objects. """
    return value.strftime(format)

env.filters['strftime'] = do_strftime

templates = [
    "welcome.html",
    "install.html",
    "teach.html",
    "compute.html",
    "codes.html",
    "conferences.html",
]

out_dir = "output"
if not os.path.exists(out_dir):
    os.mkdir(out_dir)

for template in templates:
    t = env.get_template(template)
    open(os.path.join(out_dir, template), "w").write(t.render(news=news))

