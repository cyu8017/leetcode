# LeetCode 3487 - Maximum Unique Subarray Sum After Deletion
# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/

# @param {Integer[]} nums
# @return {Integer}
def max_sum(nums)
  seen = {}
  s = 0
  has_pos = false
  max_neg = -10**9
  nums.each do |x|
    if x < 0
      max_neg = x if x > max_neg
      next
    end
    has_pos = true
    unless seen[x]
      seen[x] = true
      s += x
    end
  end
  has_pos ? s : max_neg
end
