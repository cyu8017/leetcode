# LeetCode 1015 - Smallest Integer Divisible by K
# https://leetcode.com/problems/smallest-integer-divisible-by-k/

# @param {Integer} k
# @return {Integer}
def smallest_repunit_div_by_k(k)
  return -1 if k.even? || (k % 5).zero?

  rem = 0
  (1..k).each do |length|
    rem = (rem * 10 + 1) % k
    return length if rem.zero?
  end
  -1
end
