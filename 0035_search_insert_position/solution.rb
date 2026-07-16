# LeetCode 0035 - Search Insert Position
# https://leetcode.com/problems/search-insert-position/

# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def search_insert(nums, target)
  left = 0
  right = nums.length

  while left < right
    mid = (left + right) / 2
    if nums[mid] < target
      left = mid + 1
    else
      right = mid
    end
  end

  left
end
