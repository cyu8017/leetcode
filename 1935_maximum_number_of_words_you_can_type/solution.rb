# LeetCode 1935 - Maximum Number of Words You Can Type
# https://leetcode.com/problems/maximum-number-of-words-you-can-type/

# @param {String} text
# @param {String} broken_letters
# @return {Integer}
def can_be_typed_words(text, broken_letters)
  broken = broken_letters.chars.to_h { |c| [c, true] }
  text.split.count { |w| w.chars.none? { |ch| broken[ch] } }
end
