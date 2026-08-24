# LeetCode 0905 - Sort Array By Parity
# https://leetcode.com/problems/sort-array-by-parity/

# @param {Integer[]} nums
# @return {Integer[]}
def sort_array_by_parity(nums)
  i = 0
  nums.each_with_index do |x, j|
    if x.even?
      nums[i], nums[j] = nums[j], nums[i]
      i += 1
    end
  end
  nums
end
