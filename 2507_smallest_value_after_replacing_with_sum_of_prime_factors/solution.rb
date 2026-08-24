# LeetCode 2507 - Smallest Value After Replacing With Sum of Prime Factors
# https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

# @param {Integer} n
# @return {Integer}
def smallest_value(n)
  sum_prime_factors = lambda do |x|
    s = 0
    i = 2
    while i * i <= x
      while x % i == 0
        s += i
        x /= i
      end
      i += 1
    end
    s += x if x > 1
    s
  end

  loop do
    s = sum_prime_factors.call(n)
    return n if s == n

    n = s
  end
end
