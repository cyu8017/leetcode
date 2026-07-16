# LeetCode 0412 - Fizz Buzz
# https://leetcode.com/problems/fizz-buzz/

class Solution
  def fizz_buzz(n)
    (1..n).map do |value|
      if value % 15 == 0
        "FizzBuzz"
      elsif value % 3 == 0
        "Fizz"
      elsif value % 5 == 0
        "Buzz"
      else
        value.to_s
      end
    end
  end

  alias_method :fizzBuzz, :fizz_buzz
end
