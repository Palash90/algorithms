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


# Load the input configuration for the midi to be generated
inputFile = open('input.json')
config = json.load(inputFile)

chordbotTemplateFile = open('ChordbotTemplate.json')
chordbotTemplate = json.load(chordbotTemplateFile)

# create your MIDI object
mf = MIDIFile(1)  # only 1 track
track = 0  # the only track

time = 0  # start at the beginning
mf.addTrackName(track, time, config['name'])
mf.addTempo(track, time, config["tempo"])

# add some notes
channel = 0
volume = 100

outputChords = []

choices = list(range(config['length']))
random.shuffle(choices)

numOfChords = len(config['chords'])
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

    for j in range(len(combination)):
        chord = config['chords'][combination[j]]

        chordbotSignature = chord['chordbotSignature']
        chordbotSignature['duration'] = config["numOfBar"]
        outputChords.append(chordbotSignature)

        lowOctaveNotes = chord['lowOctaveNotes']
        middleOctaveNotes = chord['middleOctaveNotes']
        highOctaveNotes = chord['highOctaveNotes']
        passingNotes = chord['passingNotes']

        totalNotes = lowOctaveNotes + middleOctaveNotes + highOctaveNotes

        filteredNotes = []
        for note in totalNotes:
            if config["noteRangeLow"] <= note <= config["noteRangeHigh"]:
                filteredNotes.append(note)

        permutedNotes = permutations(filteredNotes)
        random.shuffle(permutedNotes)
        chosenNoteSequence = permutedNotes[0]

        L = list(sums(len(filteredNotes), config['numOfBar'] * 2))
        random.shuffle(L)
        chosenDurationSequence = L[0]

        for noteCounter in range(len(chosenNoteSequence)):
            note = chosenNoteSequence[noteCounter]
            duration = chosenDurationSequence[noteCounter]

            passingNote = None

            if passingNotes is not None and noteCounter > 0:
                lastNote = chosenNoteSequence[noteCounter - 1]
                passingNoteArr = []
                for passing in passingNotes:
                    if lastNote <= passing <= note:
                        passingNoteArr.append(passing)
                random.shuffle(passingNoteArr)
                if len(passingNoteArr) > 0:
                    passingNote = passingNoteArr[0]
                    if config['noteRangeLow'] <= passingNote <= config['noteRangeHigh']:
                        pass
                    else:
                        passingNote = None

            if duration == 0:
                continue
            else:
                if duration <= 2:
                    addPassing = bool(random.getrandbits(1))
                    if addPassing and passingNote is not None:
                        mf.addNote(track, channel, passingNote, time, duration * 0.5, volume)
                        time = time + duration * 0.5
                    else:
                        mf.addNote(track, channel, note, time, duration * 0.5, volume)
                        time = time + duration * 0.5
                else:
                    fullNotes = int(duration / 2)
                    halfNote = int(duration % 2)

                    if passingNote is not None:
                        mf.addNote(track, channel, passingNote, time, 1, volume)
                    else:
                        mf.addNote(track, channel, note, time, 1, volume)
                    time = time + 1

                    for fullNote in range(fullNotes - 1):
                        mf.addNote(track, channel, note, time, 1, volume)
                        time = time + 1
                    if halfNote != 0:
                        mf.addNote(track, channel, note, time, 0.5, volume)
                        time = time + 0.5

chordbotTemplate["tempo"] = config["tempo"]
chordbotTemplate['songName'] = config["name"]
chordbotTemplate['sections'][0]["chords"] = outputChords

# write it to disk
with open(config['dir'] + config['name'] + ".midi", 'wb') as outputFile:
    mf.writeFile(outputFile)

with open(config['dir'] + config['name'] + ".json", 'w') as outputFile:
    json.dump(chordbotTemplate, outputFile)
