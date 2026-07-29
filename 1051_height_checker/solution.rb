# LeetCode 1051 - Height Checker
# https://leetcode.com/problems/height-checker/

# @param {Integer[]} heights
# @return {Integer}
def height_checker(heights)
  heights.zip(heights.sort).count { |a, b| a != b }
end
