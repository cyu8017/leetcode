# LeetCode 0507 - Perfect Number
# https://leetcode.com/problems/perfect-number/

class Solution
  def check_perfect_number(num)
    return false if num <= 1

    total = 1
    limit = Math.sqrt(num).to_i
    (2..limit).each do |divisor|
      next unless (num % divisor).zero?

      total += divisor
      pair = num / divisor
      total += pair unless pair == divisor
    end
    total == num
  end

  alias_method :checkPerfectNumber, :check_perfect_number
end
