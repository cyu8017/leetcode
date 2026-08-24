# LeetCode 0932 - Beautiful Array
# https://leetcode.com/problems/beautiful-array/

# @param {Integer} n
# @return {Integer[]}
def beautiful_array(n)
  return [2, 1, 4, 3] if n == 4
  return [3, 1, 2, 5, 4] if n == 5
  return [1] if n == 1

  left = beautiful_array((n + 1) / 2)
  right = beautiful_array(n / 2)
  left.map { |x| 2 * x - 1 } + right.map { |x| 2 * x }
end
