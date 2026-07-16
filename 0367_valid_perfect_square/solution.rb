# LeetCode 0367 - Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/

class Solution
  def is_perfect_square(num)
    left = 1
    right = num

    while left <= right
      mid = (left + right) / 2
      square = mid * mid
      return true if square == num
      if square < num
        left = mid + 1
      else
        right = mid - 1
      end
    end

    false
  end

  alias_method :isPerfectSquare, :is_perfect_square
end
