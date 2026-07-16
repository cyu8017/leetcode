# LeetCode 0085 - Maximal Rectangle
# https://leetcode.com/problems/maximal-rectangle/

# @param {Character[][]} matrix
# @return {Integer}
def maximal_rectangle(matrix)
  return 0 if matrix.nil? || matrix.empty?

  cols = matrix[0].length
  heights = Array.new(cols, 0)
  max_area = 0

  matrix.each do |row|
    cols.times do |j|
      heights[j] = row[j] == '1' ? heights[j] + 1 : 0
    end
    max_area = [max_area, largest_histogram(heights)].max
  end

  max_area
end

def largest_histogram(heights)
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
