#!/usr/bin/env python
# -*- encoding: utf-8 -*-

my_input = open("../data/generated.txt", "r")
my_output = open("../data/detokenised.txt", "a")

for line in my_input:
    eos_new_line = line.replace("<eos> ", "\n\n")
    my_output.write(eos_new_line.replace(" ", ""))
