# LeetCode 3837 - Delayed Count of Equal Elements
# https://leetcode.com/problems/delayed-count-of-equal-elements/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[]}
def delayed_count(nums, k)
  n = nums.length
  cnt = Hash.new(0)
  ans = Array.new(n, 0)
  (n - k - 2).downto(0) do |i|
    key = nums[i + k + 1]
    cnt[key] += 1
    ans[i] = cnt[nums[i]]
  end
  ans
end
