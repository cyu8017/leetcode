# LeetCode 0747 - Largest Number At Least Twice of Others
# https://leetcode.com/problems/largest-number-at-least-twice-of-others/

# @param {Integer[]} nums
# @return {Integer}
def dominant_index(nums)
  first = -1
  second = -1
  index = -1
  nums.each_with_index do |num, i|
    if num > first
      second = first
      first = num
      index = i
    elsif num > second
      second = num
    end
  end
  first >= 2 * second ? index : -1
end
