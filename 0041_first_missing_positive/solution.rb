# LeetCode 0041 - First Missing Positive
# https://leetcode.com/problems/first-missing-positive/

# @param {Integer[]} nums
# @return {Integer}
def first_missing_positive(nums)
  n = nums.length
  i = 0

  while i < n
    value = nums[i]
    target = value - 1
    if value >= 1 && value <= n && nums[target] != value
      nums[i], nums[target] = nums[target], nums[i]
    else
      i += 1
    end
  end

  (0...n).each do |index|
    return index + 1 if nums[index] != index + 1
  end

  n + 1
end
