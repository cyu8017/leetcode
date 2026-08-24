# LeetCode 2789 - Largest Element in an Array after Merge Operations
# https://leetcode.com/problems/largest-element-in-an-array-after-merge-operations/

# @param {Integer[]} nums
# @return {Integer}
def max_array_value(nums)
  n = nums.length
  cur = nums[n - 1]
  ans = cur
  (n - 2).downto(0) do |i|
    cur = nums[i] <= cur ? cur + nums[i] : nums[i]
    ans = [ans, cur].max
  end
  ans
end
