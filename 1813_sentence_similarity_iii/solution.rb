
# @param {String} sentence1
# @param {String} sentence2
# @return {Boolean}
def are_sentences_similar(sentence1, sentence2)
  words1 = sentence1.split
  words2 = sentence2.split
  n1 = words1.length
  n2 = words2.length

  i = 0
  i += 1 while i < n1 && i < n2 && words1[i] == words2[i]
  return true if i == n1 || i == n2

  j1 = n1 - 1
  j2 = n2 - 1
  while j1 >= i && j2 >= i && words1[j1] == words2[j2]
    j1 -= 1
    j2 -= 1
  end
  j1 < i || j2 < i
end
