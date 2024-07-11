
def ReverseSentence(Sentence):
    Words = Sentence.split()
    Reversed_Words = []
    for Word in Words:
        Reversed_Words.insert(0, Word)
    ReverseSentence= ' '.join(Reversed_Words)
    return ReverseSentence
Sentence = "Python is fun"
output = ReverseSentence(Sentence)
print(output)
