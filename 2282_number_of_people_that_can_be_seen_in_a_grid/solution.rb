# LeetCode 2282 - Number of People That Can Be Seen in a Grid
# https://leetcode.com/problems/number-of-people-that-can-be-seen-in-a-grid/

# @param {Integer[][]} heights
# @return {Integer[][]}
def see_people(heights)
  m = heights.length
  n = heights[0].length
  ans = Array.new(m) { Array.new(n, 0) }
  m.times do |i|
    stack = []
    (n - 1).downto(0) do |j|
      cnt = 0
      while !stack.empty? && heights[i][stack[-1]] < heights[i][j]
        stack.pop
        cnt += 1
      end
      cnt += 1 unless stack.empty?
      ans[i][j] += cnt
      stack.pop while !stack.empty? && heights[i][stack[-1]] == heights[i][j]
      stack << j
    end
  end
  n.times do |j|
    stack = []
    (m - 1).downto(0) do |i|
      cnt = 0
      while !stack.empty? && heights[stack[-1]][j] < heights[i][j]
        stack.pop
        cnt += 1
      end
      cnt += 1 unless stack.empty?
      ans[i][j] += cnt
      stack.pop while !stack.empty? && heights[stack[-1]][j] == heights[i][j]
      stack << i
    end
  end
  ans
end

alias solve see_people
