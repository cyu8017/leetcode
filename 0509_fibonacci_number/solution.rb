# LeetCode 0509 - Fibonacci Number
# https://leetcode.com/problems/fibonacci-number/

class Solution
  def fib(n)
    return n if n <= 1

    previous = 0
    current = 1
    (2..n).each do
      previous, current = current, previous + current
    end
    current
  end
end
