# Level 1
print("-------Frequency Counter-------")

from collections import Counter
s = "leetcodepractice"

most_frequent_char = Counter(s)
print(most_frequent_char)
print(most_frequent_char.most_common(1))
print(most_frequent_char.most_common(1)[0][0])

print(max(most_frequent_char, key=most_frequent_char.get))

keyFind = ""
valFind = 0
for key, val in most_frequent_char.items():
    if val > valFind:
        valFind = val
        keyFind = key
print(keyFind)

# First Unique Character in a String
for char in s:
    for key, val in most_frequent_char.items():
        if key == char and val == 1:
            print(key)
            break
    break

print("-------Anagram Checker-------")
# Anagram definition: the same length, Each character appears the same number of times

s = "listen"
t = "silent"

sCharFreq = Counter(s)
tCharFreq = Counter(t)

if sCharFreq == tCharFreq:
    print(True)
else:
    print(False)

print("-------Group Anagrams (VERY IMPORTANT)-------")

words = ["eat","tea","tan","ate","nat","bat"]

print(sorted("tea"))

