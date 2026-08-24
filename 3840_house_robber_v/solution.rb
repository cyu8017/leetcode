# LeetCode 3840 - House Robber V
# https://leetcode.com/problems/house-robber-v/

# @param {Integer[]} nums
# @param {Integer[]} colors
# @return {Integer}
def rob(nums, colors)
  n = nums.length
  f = 0
  g = nums[0]
  (1...n).each do |i|
    if colors[i - 1] == colors[i]
      nf = [f, g].max
      g = f + nums[i]
      f = nf
    else
      nf = [f, g].max
      g = nf + nums[i]
      f = nf
    end
  end
  [f, g].max
end
