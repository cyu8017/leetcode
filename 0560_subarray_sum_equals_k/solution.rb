# LeetCode 0560 - Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def subarray_sum(nums, k)
  counts = Hash.new(0)
  counts[0] = 1
  prefix = 0
  answer = 0
  nums.each do |num|
    prefix += num
    answer += counts[prefix - k]
    counts[prefix] += 1
  end
  answer
end
