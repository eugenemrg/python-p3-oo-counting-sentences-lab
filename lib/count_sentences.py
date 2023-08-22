import re

class MyString:
  def __init__(self, value = ''):
    self._value = value
  
  def get_string(self):
    return self._value
  
  def set_string(self, value):
    if type(value) == str:
      self._value = value
    else:
      print("The value must be a string.")
      
  def is_sentence(self):
    return '.' == self._value[-1]
  
  def is_question(self):
    return '?' == self._value[-1]
  
  def is_exclamation(self):
    return '!' == self._value[-1]
  
  def count_sentences(self):
    return len(re.findall("([\\w ,]+)[.+?+!+]", self._value))
      
  value = property(get_string, set_string)
  # pass
