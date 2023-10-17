import re
sentence = "The quick brown fox jumps over the lazy dog"
pos_rules = [
    (r'\bThe\b', 'DT'),            
    (r'\bquick\b', 'JJ'),           
    (r'\bbrown\b', 'JJ'),           
    (r'\bfox\b', 'NN'),         
    (r'\bjumps\b', 'VB'),         
    (r'\bover\b', 'IN'),           
    (r'\bthe\b', 'DT'),            
    (r'\blazy\b', 'JJ'),            
    (r'\bdog\b', 'NN')              
]
words = sentence.split()
pos_tags = []
for word in words:
    for pattern, pos_tag in pos_rules:
        if re.search(pattern, word, re.IGNORECASE):
            pos_tags.append((word, pos_tag))
            break
    else:
        pos_tags.append((word, 'NN'))  
print(pos_tags)
