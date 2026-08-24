# LeetCode 2091 - Removing Minimum and Maximum From Array
# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

# @param {Integer[]} nums
# @return {Integer}
def minimum_deletions(nums)
  n = nums.length
  mi = ma = 0
  nums.each_with_index do |x, i|
    mi = i if x < nums[mi]
    ma = i if x > nums[ma]
  end
  mi, ma = ma, mi if mi > ma
  [ma + 1, n - mi, mi + 1 + n - ma].min
end
