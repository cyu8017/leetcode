# LeetCode 1991 - Find the Middle Index in Array
# https://leetcode.com/problems/find-the-middle-index-in-array/

# @param {Integer[]} nums
# @return {Integer}
def find_middle_index(nums)
  total = nums.sum
  left = 0
  nums.each_with_index do |x, i|
    return i if left == total - left - x
    left += x
  end
  -1
end
