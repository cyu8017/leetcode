# LeetCode 2735 - Collecting Chocolates
# https://leetcode.com/problems/collecting-chocolates/

# @param {Integer[]} nums
# @param {Integer} x
# @return {Integer}
def min_cost(nums, x)
  n = nums.length
  best = nums.dup
  ans = nums.sum
  (1...n).each do |rot|
    cur = rot * x
    (0...n).each do |i|
      best[i] = [best[i], nums[(i + rot) % n]].min
      cur += best[i]
    end
    ans = [ans, cur].min
  end
  ans
end
