# LeetCode 2068 - Check Whether Two Strings are Almost Equivalent
# https://leetcode.com/problems/check-whether-two-strings-are-almost-equivalent/

# @param {String} word1
# @param {String} word2
# @return {Boolean}
def check_almost_equivalent(word1, word2)
  freq = Array.new(26, 0)
  word1.length.times do |i|
    freq[word1[i].ord - 97] += 1
    freq[word2[i].ord - 97] -= 1
  end
  freq.all? { |v| v.between?(-3, 3) }
end
