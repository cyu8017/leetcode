# LeetCode 0191 - Number of 1 Bits
class Solution
  def hamming_weight(n)
    count = 0
    while n != 0
      n &= n - 1
      count += 1
    end
    count
  end
end