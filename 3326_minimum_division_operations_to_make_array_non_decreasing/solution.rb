# LeetCode 3326 - Minimum Division Operations to Make Array Non Decreasing
# https://leetcode.com/problems/minimum-division-operations-to-make-array-non-decreasing/

# @param {Integer} x
# @return {Integer}
def smallest_proper_divisor(x)
  d = 2
  while d * d <= x
    return d if x % d == 0

    d += 1
  end
  x
end

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  ops = 0
  (nums.length - 2).downto(0) do |i|
    next if nums[i] <= nums[i + 1]

    while nums[i] > nums[i + 1]
      d = smallest_proper_divisor(nums[i])
      return -1 if d == nums[i]

      nums[i] = nums[i] / d
      ops += 1
      return -1 if nums[i] > nums[i + 1] && smallest_proper_divisor(nums[i]) == nums[i]
    end
  end
  ops
end
