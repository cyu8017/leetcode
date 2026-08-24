# LeetCode 3610 - Minimum Number of Primes to Sum to Target
# https://leetcode.com/problems/minimum-number-of-primes-to-sum-to-target/

$primes3610 = []

def ensure_primes3610
  return unless $primes3610.empty?
  x = 2
  while $primes3610.length < 1000
    is_prime = true
    $primes3610.each do |p|
      break if p * p > x
      if x % p == 0
        is_prime = false
        break
      end
    end
    $primes3610 << x if is_prime
    x += 1
  end
end

# @param {Integer} n
# @param {Integer} m
# @return {Integer}
def min_number_of_primes(n, m)
  ensure_primes3610
  inf = 2147483647 / 2
  f = Array.new(n + 1, inf)
  f[0] = 0
  (0...m).each do |pi|
    x = $primes3610[pi]
    (x..n).each { |i| f[i] = f[i - x] + 1 if f[i - x] + 1 < f[i] }
  end
  f[n] < inf ? f[n] : -1
end
