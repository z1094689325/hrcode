#!/usr/bin/env python
# -*- coding: utf-8 -*-

import untangle

obj = untangle.parse("./data.xml")
    
name = obj.set.l.p[1]['name']

print(name)