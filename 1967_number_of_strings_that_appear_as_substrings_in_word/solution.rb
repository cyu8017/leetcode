# LeetCode 1967 - Number of Strings That Appear as Substrings in Word
# https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/

# @param {String[]} patterns
# @param {String} word
# @return {Integer}
def num_of_strings(patterns, word)
  patterns.count { |p| word.include?(p) }
end
