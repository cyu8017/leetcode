# LeetCode 1897 - Redistribute Characters to Make All Strings Equal
# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/

# @param {String[]} words
# @return {Boolean}
def make_equal(words)
  counts = Hash.new(0)
  words.each { |word| word.each_char { |ch| counts[ch] += 1 } }
  n = words.length
  counts.values.all? { |total| total % n == 0 }
end
