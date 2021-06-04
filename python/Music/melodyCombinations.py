import json
import random

from midiutil.MidiFile import MIDIFile


def sums(length, total_sum):
    if length == 1:
        yield (total_sum,)
    else:
        for value in range(total_sum + 1):
            for permutation in sums(length - 1, total_sum - value):
                yield (value,) + permutation


def permutations(lst):
    if len(lst) <= 1:
        return [lst]  # [[X]]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remlst = lst[:i] + lst[i + 1:]
        for p in permutations(remlst):
            l.append([m] + p)
    return l  # return at end of outer for loop


# create your MIDI object
mf = MIDIFile(1)  # only 1 track
track = 0  # the only track

time = 0  # start at the beginning
mf.addTrackName(track, time, "Sample Track")
mf.addTempo(track, time, 120)

# add some notes
channel = 0
volume = 100

time = 0

inputFile = open('input.json')
inp = json.load(inputFile)

choices = list(range(inp['length']))
random.shuffle(choices)

numOfChords = len(inp['chords'])
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
        chord = inp['chords'][combination[j]]

        lowOctaveNotes = chord['lowOctaveNotes']
        middleOctaveNotes = chord['middleOctaveNotes']
        highOctaveNotes = chord['highOctaveNotes']

        totalNotes = lowOctaveNotes + middleOctaveNotes + highOctaveNotes

        filteredNotes = []
        for note in totalNotes:
            if inp["noteRangeLow"] <= note <= inp["noteRangeHigh"]:
                filteredNotes.append(note)

        permutedNotes = permutations(filteredNotes)
        random.shuffle(permutedNotes)
        chosenNoteSequence = permutedNotes[0]

        L = list(sums(len(filteredNotes), inp['numOfBar'] * 2))
        random.shuffle(L)
        chosenDurationSequence = L[0]

        print(chosenNoteSequence, chosenDurationSequence)
        for noteCounter in range(len(chosenNoteSequence)):
            note = chosenNoteSequence[noteCounter]
            duration = chosenDurationSequence[noteCounter]
            if duration == 0:
                continue
            mf.addNote(track, channel, note, time, duration * 0.5, volume)
            time = time + duration * 0.5

# write it to disk
with open("output.mid", 'wb') as outputFile:
    mf.writeFile(outputFile)
