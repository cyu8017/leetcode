# LeetCode 3355 - Zero Array Transformation I
# https://leetcode.com/problems/zero-array-transformation-i/

# @param {Integer[]} nums
# @param {Integer[][]} queries
# @return {Boolean}
def is_zero_array(nums, queries)
  n = nums.length
  diff = Array.new(n + 1, 0)
  queries.each do |q|
    diff[q[0]] += 1
    diff[q[1] + 1] -= 1
  end
  cur = 0
  n.times do |i|
    cur += diff[i]
    return false if cur < nums[i]
  end
  true
end
