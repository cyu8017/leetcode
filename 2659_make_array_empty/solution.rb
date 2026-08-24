# LeetCode 2659 - Make Array Empty
# https://leetcode.com/problems/make-array-empty/

# @param {Integer[]} nums
# @return {Integer}
def count_operations_to_empty_array(nums)
  n = nums.length
  idx = (0...n).to_a
  idx.sort_by! { |i| nums[i] }
  ans = n
  (1...n).each { |i| ans += n - i if idx[i] < idx[i - 1] }
  ans
end
