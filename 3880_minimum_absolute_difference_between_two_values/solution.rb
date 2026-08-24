# LeetCode 3880 - Minimum Absolute Difference Between Two Values
# https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

# @param {Integer[]} nums
# @return {Integer}
def min_absolute_difference(nums)
  n = nums.length
  ans = n + 1
  last = [-ans, -ans, -ans]
  n.times do |i|
    x = nums[i]
    if x != 0
      ans = [ans, i - last[3 - x]].min
      last[x] = i
    end
  end
  return -1 if ans > n
  ans
end
