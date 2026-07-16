# LeetCode 0461 - Hamming Distance
# https://leetcode.com/problems/hamming-distance/

class Solution
  def hamming_distance(x, y)
    (x ^ y).to_s(2).count("1")
  end

  alias_method :hammingDistance, :hamming_distance
end
