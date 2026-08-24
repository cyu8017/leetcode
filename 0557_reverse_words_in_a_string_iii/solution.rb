# LeetCode 0557 - Reverse Words in a String III
# https://leetcode.com/problems/reverse-words-in-a-string-iii/

# @param {String} s
# @return {String}
def reverse_words(s)
  s.split(" ", -1).map(&:reverse).join(" ")
end
