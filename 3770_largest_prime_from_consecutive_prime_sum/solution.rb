# LeetCode 3770 - Largest Prime from Consecutive Prime Sum
# https://leetcode.com/problems/largest-prime-from-consecutive-prime-sum/

# @param {Integer} n
# @return {Integer}
def largest_prime(n)
  mx = 500000
  is_prime = Array.new(mx + 1, true)
  is_prime[0] = is_prime[1] = false
  primes = []
  (2..mx).each do |i|
    next unless is_prime[i]
    primes << i
    if i * i <= mx
      (i * i).step(mx, i) { |j| is_prime[j] = false }
    end
  end
  s = [0]
  t = 0
  primes.each do |x|
    t += x
    break if t > mx
    s << t if is_prime[t]
  end
  lo = 0
  hi = s.length
  while lo < hi
    mid = (lo + hi) >> 1
    if s[mid] <= n
      lo = mid + 1
    else
      hi = mid
    end
  end
  s[lo - 1]
end
