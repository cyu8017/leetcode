# LeetCode 0869 - Reordered Power of 2
# https://leetcode.com/problems/reordered-power-of-2/

# @param {Integer} n
# @return {Boolean}
def reordered_power_of2(n)
  target = n.to_s.chars.sort
  (0...31).any? { |i| (1 << i).to_s.chars.sort == target }
end
