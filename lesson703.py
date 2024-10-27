class WordsFinder:
  def __init__(self, *file_names: str):
    self.file_names = file_names

  def get_all_words(self):
    all_words = {}
    for file_name in self.file_names:
      with open(file_name, 'r') as file:
        words = file.read().split()
        all_words.update({file_name: [
          word.lower().translate(str.maketrans(
            '', '', ',.=!?;: - ')) for word in words]})
    return all_words

  def find(self, word: str):
    all_words = self.get_all_words()
    result = {}
    for file_name, words in all_words.items():
      for i, w in enumerate(words):
        if w == word.lower():
          result[file_name] = i + 1
          break
    return result

  def count(self, word: str):
    all_words = self.get_all_words()
    result = {}
    for file_name, words in all_words.items():
      count = 0
      for w in words:
        if w == word.lower():
          count += 1
      result[file_name] = count
    return result

finder1 = WordsFinder('My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
