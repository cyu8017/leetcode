# LeetCode 1742 - Maximum Number of Balls in a Box
# https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

# @param {Integer} low_limit
# @param {Integer} high_limit
# @return {Integer}
def count_balls(low_limit, high_limit)
  counts = Hash.new(0)
  (low_limit..high_limit).each do |value|
    box = value.digits.sum
    counts[box] += 1
  end
  counts.values.max
end
