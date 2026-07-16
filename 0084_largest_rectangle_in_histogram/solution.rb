# LeetCode 0084 - Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/

# @param {Integer[]} heights
# @return {Integer}
def largest_rectangle_area(heights)
  stack = []
  max_area = 0
  extended = heights + [0]

  extended.each_with_index do |height, i|
    while !stack.empty? && extended[stack[-1]] > height
      h = extended[stack.pop]
      width = stack.empty? ? i : i - stack[-1] - 1
      max_area = [max_area, h * width].max
    end
    stack << i
  end

  max_area
end
