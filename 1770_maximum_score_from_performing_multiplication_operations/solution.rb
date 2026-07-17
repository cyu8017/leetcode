# LeetCode 1770 - Maximum Score from Performing Multiplication Operations
# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/

# @param {Integer[]} nums
# @param {Integer[]} multipliers
# @return {Integer}
def maximum_score(nums, multipliers)
  n = nums.length
  m = multipliers.length
  next_row = Array.new(m + 1, 0)
  (m - 1).downto(0) do |i|
    cur = Array.new(m + 1, 0)
    i.downto(0) do |left|
      right = n - 1 - (i - left)
      take_left = nums[left] * multipliers[i] + next_row[left + 1]
      take_right = nums[right] * multipliers[i] + next_row[left]
      cur[left] = [take_left, take_right].max
    end
    next_row = cur
  end
  next_row[0]
end
