# LeetCode 2672 - Number of Adjacent Elements With the Same Color
# https://leetcode.com/problems/number-of-adjacent-elements-with-the-same-color/

# @param {Integer} n
# @param {Integer[][]} queries
# @return {Integer[]}
def color_the_array(n, queries)
  colors = Array.new(n, 0)
  ans = Array.new(queries.length, 0)
  same = 0
  queries.each_with_index do |(idx, color), i|
    if colors[idx] != 0
      same -= 1 if idx > 0 && colors[idx] == colors[idx - 1]
      same -= 1 if idx + 1 < n && colors[idx] == colors[idx + 1]
    end
    colors[idx] = color
    same += 1 if idx > 0 && colors[idx] == colors[idx - 1]
    same += 1 if idx + 1 < n && colors[idx] == colors[idx + 1]
    ans[i] = same
  end
  ans
end
