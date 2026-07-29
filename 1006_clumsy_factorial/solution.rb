# LeetCode 1006 - Clumsy Factorial
# https://leetcode.com/problems/clumsy-factorial/

# @param {Integer} n
# @return {Integer}
def clumsy(n)
  stack = [n]
  n -= 1
  op = 0
  while n > 0
    case op % 4
    when 0
      stack << (stack.pop * n)
    when 1
      stack << (stack.pop.to_f / n).to_i
    when 2
      stack << n
    else
      stack << -n
    end
    n -= 1
    op += 1
  end
  stack.sum
end
