# LeetCode 3068 - Find the Maximum Sum of Node Values
# https://leetcode.com/problems/find-the-maximum-sum-of-node-values/

# @param {Integer[]} nums
# @param {Integer} k
# @param {Integer[][]} edges
# @return {Integer}
def maximum_value_sum(nums, k, edges)
  f0 = 0
  f1 = -(1 << 53)
  nums.each do |x|
    nf0 = [f0 + x, f1 + (x ^ k)].max
    nf1 = [f1 + x, f0 + (x ^ k)].max
    f0 = nf0
    f1 = nf1
  end
  f0
end
