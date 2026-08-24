# LeetCode 3496 - Maximize Score After Pair Deletions
# https://leetcode.com/problems/maximize-score-after-pair-deletions/

# @param {Integer[]} nums
# @return {Integer}
def maximize_score(nums)
  n = nums.length
  total = 0
  nums.each { |x| total += x }
  if n.odd?
    mn = nums[0]
    nums.each { |x| mn = x if x < mn }
    return total - mn
  end
  mn = nums[0] + nums[1]
  (0...(n - 1)).each { |i| mn = [mn, nums[i] + nums[i + 1]].min }
  total - mn
end
