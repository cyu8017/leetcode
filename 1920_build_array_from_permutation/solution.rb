# LeetCode 1920 - Build Array from Permutation
# https://leetcode.com/problems/build-array-from-permutation/

# @param {Integer[]} nums
# @return {Integer[]}
def build_array(nums)
  nums.map { |x| nums[x] }
end
