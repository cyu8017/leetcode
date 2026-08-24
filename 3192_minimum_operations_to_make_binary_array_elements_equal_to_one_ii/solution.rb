# LeetCode 3192 - Minimum Operations to Make Binary Array Elements Equal to One II
# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-ii/

# @param {Integer[]} nums
# @return {Integer}
def min_operations(nums)
  ans = 0
  v = 0
  nums.each do |raw|
    x = raw ^ v
    if x == 0
      v ^= 1
      ans += 1
    end
  end
  ans
end
