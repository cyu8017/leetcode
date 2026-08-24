# LeetCode 2966 - Divide Array Into Arrays With Max Difference
# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/

# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer[][]}
def divide_array(nums, k)
  nums.sort!
  ans = []
  i = 0
  while i < nums.length
    return [] if nums[i + 2] - nums[i] > k

    ans << [nums[i], nums[i + 1], nums[i + 2]]
    i += 3
  end
  ans
end
