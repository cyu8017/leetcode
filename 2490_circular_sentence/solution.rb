# LeetCode 2490 - Circular Sentence
# https://leetcode.com/problems/circular-sentence/

# @param {String} sentence
# @return {Boolean}
def is_circular_sentence(sentence)
  n = sentence.length
  return false if sentence[0] != sentence[n - 1]

  (0...n).each do |i|
    return false if sentence[i] == " " && sentence[i - 1] != sentence[i + 1]
  end
  true
end
