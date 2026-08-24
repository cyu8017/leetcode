# LeetCode 3375 - Minimum Operations to Make Array Values Equal to K
# https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def min_operations(nums, k)
  seen = {}
  nums.each do |x|
    return -1 if x < k

    seen[x] = true if x > k
  end
  seen.length
end
