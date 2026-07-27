# LeetCode 1674 - Minimum Moves to Make Array Complementary
# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/

# @param {Integer[]} nums
# @param {Integer} limit
# @return {Integer}
def min_moves(nums, limit)
  n = nums.length
  d = Array.new(2 * limit + 2, 0)
  (n / 2).times do |i|
    a = nums[i]
    b = nums[n - 1 - i]
    lo = [a, b].min + 1
    hi = [a, b].max + limit
    s = a + b
    d[2] += 2
    d[lo] -= 1
    d[s] -= 1
    d[s + 1] += 1
    d[hi + 1] += 1
  end
  ans = 10**9
  cur = 0
  (2..(2 * limit)).each do |s|
    cur += d[s]
    ans = [ans, cur].min
  end
  ans
end
