# LeetCode 2546 - Apply Bitwise Operations to Make Strings Equal
# https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/

# @param {String} s
# @param {String} target
# @return {Boolean}
def make_strings_equal(s, target)
  has1s = false
  has1t = false
  s.length.times do |i|
    has1s = true if s[i] == "1"
    has1t = true if target[i] == "1"
  end
  has1s == has1t
end
