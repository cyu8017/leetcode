# LeetCode 3684 - Maximize Sum of At Most K Distinct Elements
# https://leetcode.com/problems/maximize-sum-of-at-most-k-distinct-elements/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def max_k_distinct(nums, k)
  nums = nums.sort
  n = nums.length
  ans = []
  (n - 1).downto(0) do |i|
    next if i + 1 < n && nums[i] == nums[i + 1]

    ans << nums[i]
    k -= 1
    break if k == 0
  end
  ans
end
