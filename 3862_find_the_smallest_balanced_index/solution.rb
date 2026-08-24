# LeetCode 3862 - Find the Smallest Balanced Index
# https://leetcode.com/problems/find-the-smallest-balanced-index/

# @param {Integer[]} nums
# @return {Integer}
def smallest_balanced_index(nums)
  s = nums.sum
  p = 1
  (nums.length - 1).downto(0) do |i|
    s -= nums[i]
    return i if s == p
    p *= nums[i]
    break if p >= s
  end
  -1
end
