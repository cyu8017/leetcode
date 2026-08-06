# LeetCode 1589 - Maximum Sum Obtained of Any Permutation
# https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/

# @param {Integer[]} nums
# @param {Integer[][]} requests
# @return {Integer}
def max_sum_range_query(nums, requests)
  mod = 1_000_000_007
  diff = Array.new(nums.length + 1, 0)
  requests.each do |left, right|
    diff[left] += 1
    diff[right + 1] -= 1
  end
  (1...nums.length).each { |i| diff[i] += diff[i - 1] }
  nums.sort.zip(diff[0...-1].sort).sum { |a, b| a * b } % mod
end
