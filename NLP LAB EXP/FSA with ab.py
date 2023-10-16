def ends_with_ab(input_string):
    state = 0
    for char in input_string:
        if state == 0:
            if char == 'a':
                state = 1
        elif state == 1:
            if char == 'b':
                state = 2
            else:
                state = 0
    return state == 2
test_string = ["ab","aab","abb","acab","abab"]
for string in test_strings:
    if ends_with_ab(string):
        print(f"'{string}'matches the pattern.")
    else:
         print(f"'{string}'does not match the pattern.")
            
