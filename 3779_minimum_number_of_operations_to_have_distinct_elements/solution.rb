# LeetCode 3779 - Minimum Number of Operations to Have Distinct Elements
# https://leetcode.com/problems/minimum-number-of-operations-to-have-distinct-elements/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  st = {}
  (nums.length - 1).downto(0) do |i|
    return i / 3 + 1 if st[nums[i]]
    st[nums[i]] = true
  end
  0
end
