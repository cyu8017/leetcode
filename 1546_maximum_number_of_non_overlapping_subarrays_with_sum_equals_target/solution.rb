# LeetCode 1546 - Maximum Number of Non-Overlapping Subarrays With Sum Equals Target
# https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def max_non_overlapping(nums, target)
  seen = { 0 => true }
  prefix = answer = 0
  nums.each do |value|
    prefix += value
    if seen[prefix - target]
      answer += 1
      prefix = 0
      seen = { 0 => true }
    else
      seen[prefix] = true
    end
  end
  answer
end
