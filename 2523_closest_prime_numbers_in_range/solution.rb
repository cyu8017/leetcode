# LeetCode 2523 - Closest Prime Numbers in Range
# https://leetcode.com/problems/closest-prime-numbers-in-range/

# @param {Integer} left
# @param {Integer} right
# @return {Integer[]}
def closest_primes(left, right)
  is_prime = Array.new(right + 1, true)
  is_prime[0] = false if right >= 0
  is_prime[1] = false if right >= 1
  i = 2
  while i * i <= right
    if is_prime[i]
      j = i * i
      while j <= right
        is_prime[j] = false
        j += i
      end
    end
    i += 1
  end
  primes = (left..right).select { |x| is_prime[x] }
  return [-1, -1] if primes.length < 2

  best_diff = 10**18
  best = [-1, -1]
  (0...primes.length - 1).each do |i|
    d = primes[i + 1] - primes[i]
    if d < best_diff
      best_diff = d
      best = [primes[i], primes[i + 1]]
    end
  end
  best
end
