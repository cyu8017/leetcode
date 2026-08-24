# LeetCode 2439 - Minimize Maximum of Array
# https://leetcode.com/problems/minimize-maximum-of-array/

# @param {Integer[]} nums
# @return {Integer}
def minimize_array_value(nums)
  total = 0
  ans = 0
  nums.each_with_index do |x, i|
    total += x
    avg = (total + i) / (i + 1)
    ans = avg if avg > ans
  end
  ans
end
