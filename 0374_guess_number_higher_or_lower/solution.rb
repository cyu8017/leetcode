# LeetCode 0374 - Guess Number Higher or Lower
# https://leetcode.com/problems/guess-number-higher-or-lower/

def guess(_num)
  0
end

class Solution
  def guess_number(n)
    left = 1
    right = n

    while left <= right
      mid = (left + right) / 2
      result = guess(mid)
      return mid if result.zero?
      if result.negative?
        right = mid - 1
      else
        left = mid + 1
      end
    end

    left
  end

  alias_method :guessNumber, :guess_number
end
