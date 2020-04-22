#!/usr/bin/env python
# -*- encoding: utf-8 -*-

my_input = open("scrape.txt", "r")
my_output = open("tokenised.txt", "a")

for line in my_input:
    my_output.write(" ".join(line))
