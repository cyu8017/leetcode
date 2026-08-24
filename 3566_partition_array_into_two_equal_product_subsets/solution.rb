# LeetCode 3566 - Partition Array into Two Equal Product Subsets
# https://leetcode.com/problems/partition-array-into-two-equal-product-subsets/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Boolean}
def check_equal_partitions(nums, target)
  n = nums.length
  (0...(1 << n)).each do |i|
    x = 1
    y = 1
    (0...n).each do |j|
      if ((i >> j) & 1) != 0
        x *= nums[j]
      else
        y *= nums[j]
      end
      break if x > target || y > target
    end
    return true if x == target && y == target
  end
  false
end
