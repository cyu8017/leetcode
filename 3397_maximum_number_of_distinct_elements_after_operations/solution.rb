# LeetCode 3397 - Maximum Number of Distinct Elements After Operations
# https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def max_distinct_elements(nums, k)
  nums = nums.sort
  ans = 0
  prev = -4_503_599_627_370_496
  nums.each do |x|
    cur = x - k
    cur = prev + 1 if cur <= prev
    next if cur > x + k

    ans += 1
    prev = cur
  end
  ans
end
