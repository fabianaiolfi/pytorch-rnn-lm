#!/usr/bin/env python
# -*- encoding: utf-8 -*-

my_input = open("../data/scraped.txt", "r")
my_output = open("../data/tokenised.txt", "a")

for line in my_input:
    my_output.write(" ".join(line))
