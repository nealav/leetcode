def uniqueMorseRepresentations(words):
            d = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
            return len({''.join(d[ord(i) - ord('a')] for i in w) for w in words})

print(uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))

'''
uses a list comprehension to append morse code transformations of words to a set
we only need unique strings so we use a set instead of a list
'''
