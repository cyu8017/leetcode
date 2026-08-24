# LeetCode 2009 - Minimum Number of Operations to Make Array Continuous
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  n = nums.length
  uniq = nums.uniq.sort
  ans = n
  j = 0
  uniq.each_index do |i|
    j += 1 while j < uniq.length && uniq[j] - uniq[i] + 1 <= n
    ans = [ans, n - (j - i)].min
  end
  ans
end
