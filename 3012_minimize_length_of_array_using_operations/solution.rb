# LeetCode 3012 - Minimize Length of Array Using Operations
# https://leetcode.com/problems/minimize-length-of-array-using-operations/

# @param {Integer[]} nums
# @return {Integer}
def minimum_array_length(nums)
  mi = nums.min
  cnt = 0
  nums.each do |x|
    return 1 if x % mi != 0

    cnt += 1 if x == mi
  end
  (cnt + 1) / 2
end
