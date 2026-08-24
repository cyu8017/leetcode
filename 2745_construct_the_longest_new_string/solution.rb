# LeetCode 2745 - Construct the Longest New String
# https://leetcode.com/problems/construct-the-longest-new-string/

# @param {Integer} x
# @param {Integer} y
# @param {Integer} z
# @return {Integer}
def longest_string(x, y, z)
  if x < y
    (2 * x + 1 + z) * 2
  elsif y < x
    (2 * y + 1 + z) * 2
  else
    (x + y + z) * 2
  end
end
