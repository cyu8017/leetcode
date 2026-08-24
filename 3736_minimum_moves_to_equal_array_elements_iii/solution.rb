# LeetCode 3736 - Minimum Moves to Equal Array Elements III
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

# @param {Integer[]} nums
# @return {Integer}
def min_moves(nums)
  mx = 0
  s = 0
  nums.each do |x|
    mx = [mx, x].max
    s += x
  end
  mx * nums.length - s
end
