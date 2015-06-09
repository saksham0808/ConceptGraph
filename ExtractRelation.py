import sys
import re

from Concept import *

if len(sys.argv) == 1:
    print("No files provided.")
    exit()

ConceptList = [Concept("Conditionals"), Concept("Loop"), Concept("Display"), Concept("Custom")]

for filename in sys.argv[1:]:
    relations = set()
    f = open(filename, 'r')
    text = f.read()

    for concept in ConceptList:
        isUnmatched = 0
        for unmatcher in concept.unmatchers:
            if re.search(unmatcher, text):
                isUnmatched = 1
                break
        if isUnmatched:
            continue
        for regex in concept.regex:
            if re.search(regex, text):
                relations.add(concept.name)

    print("File " + filename + " has relations:")
    print(relations)
