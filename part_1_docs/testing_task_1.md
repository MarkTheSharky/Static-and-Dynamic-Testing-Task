### Testing task 1:

# Carry out static testing on the code below.
# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.: 
Thinking that methods should be renamed or should be class level, or using string interpolation etc. 

These aren't errors but rather standards that vary from developer to developer. 

Only comment on errors that would stop the tests running.

```python

class CardGame:
                                            # Line 18 - Class values are not defined using __init__ method.

  def check_for_ace(self, card):
    if card.value = 1:                      # Line 21 - Comparrison operator should be double = (i.e. ==)
      return True
    else                                    # Line 23 - Else should be followed by a colon.
      return False
   

  dif highest_card(self, card1 card2):      # Line 27 - Method should be "def" not "dif". And card1 and card2 should be seperated by a comma.
  if card1.value > card2.value:             # Line 28 - Indentation for lines 28 to 31 should be indented again.
    return card                             # line 29 - card has not been defined and neither is it a string, the return should be card1.
  else:                                
    return card2
  


def cards_total(self, cards):               # Line 35 - Requires indented to be within class scope
  total                                     # Line 36 - "total" has not been defined as a variable. total = 0
  for card in cards:
    total += card.value
    return "You have a total of" + total    # Line 39 - The return statement should be outside the 'for' block.
                                            # Line 39 - Total will equal an interger, Python can not combine strings and intergers.
                                            # Line 39 - Integer will need to be converted to a string
```
