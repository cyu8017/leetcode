# LeetCode 1941 - Check if All Characters Have Equal Number of Occurrences
# https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

# @param {String} s
# @return {Boolean}
def are_occurrences_equal(s)
  freq = Hash.new(0)
  s.each_char { |c| freq[c] += 1 }
  freq.values.uniq.length == 1
end
