# LeetCode 0775 - Global and Local Inversions
# https://leetcode.com/problems/global-and-local-inversions/

# @param {Integer[]} nums
# @return {Boolean}
def is_ideal_permutation(nums)
  nums.each_with_index.all? { |value, i| (value - i).abs <= 1 }
end
