# LeetCode 0172 - Factorial Trailing Zeroes
# https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution
  def trailing_zeroes(n)
    count = 0
    while n.positive?
      n /= 5
      count += n
    end
    count
  end
end