# LeetCode 1504 - Count Submatrices With All Ones
# https://leetcode.com/problems/count-submatrices-with-all-ones/

# @param {Integer[][]} mat
# @return {Integer}
def num_submat(mat)
  ans = 0
  heights = Array.new(mat[0].length, 0)
  mat.each do |row|
    row.each_with_index do |x, j|
      heights[j] = x == 1 ? heights[j] + 1 : 0
    end
    stack = []
    running = 0
    heights.each do |h|
      count = 1
      while !stack.empty? && stack[-1][0] >= h
        old, width = stack.pop
        running -= old * width
        count += width
      end
      stack << [h, count]
      running += h * count
      ans += running
    end
  end
  ans
end
