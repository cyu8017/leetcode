# LeetCode 1968 - Array With Elements Not Equal to Average of Neighbors
# https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

# @param {Integer[]} nums
# @return {Integer[]}
def rearrange_array(nums)
  nums = nums.sort
  n = nums.length
  mid = (n + 1) / 2
  small = nums[0...mid]
  large = nums[mid..]
  ans = []
  i = j = 0
  while i < small.length || j < large.length
    if i < small.length
      ans << small[i]
      i += 1
    end
    if j < large.length
      ans << large[j]
      j += 1
    end
  end
  ans
end
