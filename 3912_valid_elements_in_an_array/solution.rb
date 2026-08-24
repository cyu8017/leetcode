# LeetCode 3912 - Valid Elements in an Array
# https://leetcode.com/problems/valid-elements-in-an-array/

# @param {Integer[]} nums
# @return {Integer[]}
def find_valid_elements(nums)
  n = nums.length
  right = Array.new(n, 0)
  right[n - 1] = nums[n - 1]
  (n - 2).downto(0) { |i| right[i] = [right[i + 1], nums[i]].max }
  left = 0
  ans = []
  n.times do |i|
    x = nums[i]
    ans << x if x > left || i == n - 1 || x > right[i + 1]
    left = [left, x].max
  end
  ans
end
