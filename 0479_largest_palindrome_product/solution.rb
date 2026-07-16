# LeetCode 0479 - Largest Palindrome Product
# https://leetcode.com/problems/largest-palindrome-product/

class Solution
  def largest_palindrome(n)
    return 9 if n == 1

    upper = 10**n - 1
    lower = 10**(n - 1)
    upper.downto(lower) do |first|
      candidate = (first.to_s + first.to_s.reverse).to_i
      factor = upper
      while factor * factor >= candidate
        if candidate % factor == 0
          partner = candidate / factor
          return candidate % 1337 if partner >= lower && partner <= upper
        end
        factor -= 1
      end
    end
    0
  end

  alias_method :largestPalindrome, :largest_palindrome
end
