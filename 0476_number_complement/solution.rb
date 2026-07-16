# LeetCode 0476 - Number Complement
# https://leetcode.com/problems/number-complement/

class Solution
  def find_complement(num)
    mask = num
    mask |= mask >> 1
    mask |= mask >> 2
    mask |= mask >> 4
    mask |= mask >> 8
    mask |= mask >> 16
    num ^ mask
  end

  alias_method :findComplement, :find_complement
end
