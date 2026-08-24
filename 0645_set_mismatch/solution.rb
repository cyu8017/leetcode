# LeetCode 0645 - Set Mismatch
# https://leetcode.com/problems/set-mismatch/

# @param {Integer[]} nums
# @return {Integer[]}
def find_error_nums(nums)
  n = nums.length
  seen = Array.new(n + 1, 0)
  duplicate = -1
  missing = -1
  nums.each { |value| seen[value] += 1 }
  (1..n).each do |value|
    if seen[value] == 2
      duplicate = value
    elsif seen[value].zero?
      missing = value
    end
  end
  [duplicate, missing]
end
