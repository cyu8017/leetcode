# LeetCode 2647 - Color the Triangle Red
# https://leetcode.com/problems/color-the-triangle-red/

# @param {Integer} n
# @return {Integer[][]}
def color_red(n)
  ans = [[1, 1]]
  (2..n).each do |i|
    ans << [i, 1]
    ans << [i, 2 * i - 1]
  end
  ans
end

def solve(*args)
  color_red(*args)
end
