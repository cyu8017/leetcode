# LeetCode 1695 - Maximum Erasure Value
# https://leetcode.com/problems/maximum-erasure-value/

# @param {Integer[]} nums
# @return {Integer}
def maximum_unique_subarray(nums)
  seen = {}
  left = 0
  cur = 0
  best = 0
  nums.each_with_index do |x, right|
    if seen.key?(x) && seen[x] >= left
      stop = seen[x]
      while left <= stop
        cur -= nums[left]
        left += 1
      end
    end
    seen[x] = right
    cur += x
    best = [best, cur].max
  end
  best
end
