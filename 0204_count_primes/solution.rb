# LeetCode 0204 - Count Primes
# https://leetcode.com/problems/count-primes/

# @param {Integer} n
# @return {Integer}
def count_primes(n)
  return 0 if n <= 2

  is_prime = Array.new(n, true)
  is_prime[0] = is_prime[1] = false
  p = 2
  while p * p < n
    if is_prime[p]
      multiple = p * p
      while multiple < n
        is_prime[multiple] = false
        multiple += p
      end
    end
    p += 1
  end
  is_prime.count(true)
end