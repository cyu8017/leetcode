# LeetCode 0166 - Fraction to Recurring Decimal
# https://leetcode.com/problems/fraction-to-recurring-decimal/

class Solution
  def fraction_to_decimal(numerator, denominator)
    return "0" if numerator.zero?

    sign = (numerator.negative? ^ denominator.negative?) ? "-" : ""
    numerator = numerator.abs
    denominator = denominator.abs
    integer, remainder = numerator.divmod(denominator)
    return "#{sign}#{integer}" if remainder.zero?

    result = ["#{sign}#{integer}", "."]
    seen = {}
    until remainder.zero?
      if seen.key?(remainder)
        result.insert(seen[remainder], "(")
        result << ")"
        break
      end
      seen[remainder] = result.length
      remainder *= 10
      digit, remainder = remainder.divmod(denominator)
      result << digit.to_s
    end
    result.join
  end
end