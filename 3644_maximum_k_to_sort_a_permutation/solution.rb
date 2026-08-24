# LeetCode 3644 - Maximum K to Sort a Permutation
# https://leetcode.com/problems/maximum-k-to-sort-a-permutation/

# @param {Integer[]} nums
# @return {Integer}
def sort_permutation(nums)
  ans = -1
  nums.each_with_index do |v, i|
    ans &= v if i != v
  end
  [ans, 0].max
end
