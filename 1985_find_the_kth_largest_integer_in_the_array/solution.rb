# LeetCode 1985 - Find the Kth Largest Integer in the Array
# https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/

# @param {String[]} nums
# @param {Integer} k
# @return {String}
def kth_largest_number(nums, k)
  nums.sort_by { |x| [x.length, x] }.reverse[k - 1]
end
