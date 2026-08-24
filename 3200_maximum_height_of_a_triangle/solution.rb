# LeetCode 3200 - Maximum Height of a Triangle
# https://leetcode.com/problems/maximum-height-of-a-triangle/

# @param {Integer} red
# @param {Integer} blue
# @return {Integer}
def max_height_of_triangle(red, blue)
  ans = 0
  (0...2).each do |k|
    colors = [red, blue]
    i = 1
    j = k
    while i <= colors[j]
      colors[j] -= i
      ans = [ans, i].max
      i += 1
      j ^= 1
    end
  end
  ans
end
