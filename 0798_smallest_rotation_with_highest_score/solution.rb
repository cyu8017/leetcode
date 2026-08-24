# LeetCode 0798 - Smallest Rotation with Highest Score
# https://leetcode.com/problems/smallest-rotation-with-highest-score/

# @param {Integer[]} nums
# @return {Integer}
def best_rotation(nums)
  n = nums.length
  change = Array.new(n, 1)
  nums.each_with_index { |value, i| change[(i - value + 1) % n] -= 1 }
  (1...n).each { |i| change[i] += change[i - 1] }
  change.index(change.max)
end
