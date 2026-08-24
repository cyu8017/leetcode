# LeetCode 2670 - Find the Distinct Difference Array
# https://leetcode.com/problems/find-the-distinct-difference-array/

# @param {Integer[]} nums
# @return {Integer[]}
def distinct_difference_array(nums)
  n = nums.length
  suf = Array.new(n + 1, 0)
  seen = {}
  (n - 1).downto(0) do |i|
    seen[nums[i]] = true
    suf[i] = seen.length
  end
  seen = {}
  ans = Array.new(n, 0)
  n.times do |i|
    seen[nums[i]] = true
    ans[i] = seen.length - suf[i + 1]
  end
  ans
end
