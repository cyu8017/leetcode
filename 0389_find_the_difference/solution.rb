# LeetCode 0389 - Find the Difference
# https://leetcode.com/problems/find-the-difference/

class Solution
  def find_the_difference(s, t)
    xor_value = 0
    (s + t).each_byte { |byte| xor_value ^= byte }
    xor_value.chr
  end

  alias_method :findTheDifference, :find_the_difference
end
