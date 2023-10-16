import re
text = "the quick brown fox jumps over the lazy dog. it's a sunny day."
pattern = r'\b\w{3}\b'
matches = re.findall(pattern,text)
print("all matches:")
print(match)
search_result = re.search(pattern,text)
if search_result:
    print("\nfirst match found:",search_result.group())
    print("\n iterating through matches:")
    re.finditer(patten,text):
        print(match.group(),"at position",match.start())
        replacement = re.sub(pattern,"###",text)
        print("\ntext with replacement:")
        print(replacement)
