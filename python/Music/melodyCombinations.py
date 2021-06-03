from midiutil.MidiFile import MIDIFile
import random
import json


def sums(length, total_sum):
    if length == 1:
        yield (total_sum,)
    else:
        for value in range(total_sum + 1):
            for permutation in sums(length - 1, total_sum - value):
                yield (value,) + permutation


inputFile = open('input.json')
input = json.load(inputFile)

choices = list(range(input['length']))
random.shuffle(choices)

numOfChords = len(input['chords'])
chordCombinations = []

if numOfChords < 3:
    print("This script will not generate expected results for less than 3 chords in input")

for i in range(numOfChords):
    for j in range(numOfChords):
        for k in range(numOfChords):
            for l in range(numOfChords):
                if i != j and i != k and i != l and j != k and j != l and k != l:
                    chordCombinations.append(tuple([i, j, k, l]))


for i in choices:
    combination = chordCombinations[i]
    for j in combination:
        chord = input['chords'][combination[j]]

        lowOctaveNotes = chord['lowOctaveNotes']
        middleOctaveNotes = chord['middleOctaveNotes']
        highOctaveNotes = chord['highOctaveNotes']

        totalNotes = lowOctaveNotes + middleOctaveNotes + highOctaveNotes

        L = list(sums(len(totalNotes), input['numOfBar']*2))
        print('total permutations:', len(L))

        # First and last 10 of list
        for i in L[:10] + L[-10:]:
            print(i)
