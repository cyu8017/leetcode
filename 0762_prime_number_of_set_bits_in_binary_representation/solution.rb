# LeetCode 0762 - Prime Number of Set Bits in Binary Representation
# https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

# @param {Integer} left
# @param {Integer} right
# @return {Integer}
def count_prime_set_bits(left, right)
  primes = { 2 => true, 3 => true, 5 => true, 7 => true, 11 => true, 13 => true, 17 => true, 19 => true }
  (left..right).count { |num| primes[num.to_s(2).count("1")] }
end
