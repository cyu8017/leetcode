# LeetCode 0070 - Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/

# @param {Integer} n
# @return {Integer}
def climb_stairs(n)
  return n if n <= 2

  prev = 1
  curr = 2

  (3..n).each do
    prev, curr = curr, prev + curr
  end

  curr
end
