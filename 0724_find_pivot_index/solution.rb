# LeetCode 0724 - Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/

# @param {Integer[]} nums
# @return {Integer}
def pivot_index(nums)
  total = nums.sum
  left = 0
  nums.each_with_index do |num, i|
    return i if left == total - left - num

    left += num
  end
  -1
end
