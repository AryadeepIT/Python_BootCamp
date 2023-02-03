bread_pieces = ["front", "mid-3a", "mid-2a", "mid-1a", "mid", "mid-1b", "mid-2b", "mid-3b", "back"]

print(bread_pieces[1:8])  # slicing between front and back
print(bread_pieces[1:])  # slice till the last
print(bread_pieces[:8])  # slice except last one
print(bread_pieces[1:8:2]) # slice position1-8 with increment val 2
print(bread_pieces[::2]) # slice from start with increment val 2
print(bread_pieces[::-2]) # reverse the slicing with decrement val 2


vowels = ("a", "e", "i", "o", "u")
print(vowels[2:5])  # slice through tuple