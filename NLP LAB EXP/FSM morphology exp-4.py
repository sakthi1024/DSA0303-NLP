class PluralFiniteStateMachine:
    def __init__(self):
        self.state = 'start'
        self.transitions = {
            'start': {'consonant': 'add_s', 'vowel':'add_es'},
            'add_s': {},
            'add_es':{},
            }
        def apply_rule(self,word):
            for char in word:
                if char.isalpha():
                    category = 'consonant' if char not in 'aeiou' else 'vowel'
                    self.state = self.transitions[self.state][category]
                    if self.state == 'add_s':
                        return word + 's'
                    elif self.state == 'add_es':
                        return word + 'es'
                    else:
                        return None
   plural_fsm = PluralFiniteStateMachine ()
   nouns = ["dog", "cat", "fish", "church"]
   for noun in nouns:
       plural_form = plural_fsm.apply_rule(noun)
       if plural_form:
           print(f"{noun} -> {plural_form}")
           else:
               print(f"no rule found for {noun}")
    
