# LeetCode 3190 - Find Minimum Operations to Make All Elements Divisible by Three
# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

# @param {Integer[]} nums
# @return {Integer}
def minimum_operations(nums)
  nums.count { |x| x % 3 != 0 }
end
