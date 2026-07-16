# LeetCode 0266 - Palindrome Permutation
# https://leetcode.com/problems/palindrome-permutation/

# @param {String} s
# @return {Boolean}
def can_permute_palindrome(s)
  counts = Array.new(26, 0)
  s.each_char { |char| counts[char.ord - 97] += 1 }
  counts.count(&:odd?) <= 1
end
