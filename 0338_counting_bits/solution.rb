# LeetCode 0338 - Counting Bits
# https://leetcode.com/problems/counting-bits/

class Solution
  def count_bits(n)
    result = Array.new(n + 1, 0)
    (1..n).each do |index|
      result[index] = result[index & (index - 1)] + 1
    end
    result
  end

  alias_method :countBits, :count_bits
end
