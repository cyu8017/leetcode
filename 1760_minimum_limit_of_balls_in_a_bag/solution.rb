# LeetCode 1760 - Minimum Limit of Balls in a Bag
# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/

# @param {Integer[]} nums
# @param {Integer} max_operations
# @return {Integer}
def minimum_size(nums, max_operations)
  lo = 1
  hi = nums.max
  while lo < hi
    mid = (lo + hi) / 2
    ops = nums.sum { |x| (x - 1) / mid }
    if ops <= max_operations
      hi = mid
    else
      lo = mid + 1
    end
  end
  lo
end
