# LeetCode 1175 - Prime Arrangements
# https://leetcode.com/problems/prime-arrangements/

# @param {Integer} n
# @return {Integer}
def num_prime_arrangements(n)
  mod = 10**9 + 7
  is_prime = lambda do |x|
    return false if x < 2
    (2..Math.sqrt(x)).none? { |d| x % d == 0 }
  end
  primes = (1..n).count { |i| is_prime.call(i) }
  fact = lambda do |x|
    r = 1
    (1..x).each { |i| r = (r * i) % mod }
    r
  end
  (fact.call(primes) * fact.call(n - primes)) % mod
end
