# LeetCode 2521 - Distinct Prime Factors of Product of Array
# https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

# @param {Integer[]} nums
# @return {Integer}
def distinct_prime_factors(nums)
  seen = {}
  nums.each do |num|
    x = num
    p = 2
    while p * p <= x
      if x % p == 0
        seen[p] = true
        x /= p while x % p == 0
      end
      p += 1
    end
    seen[x] = true if x > 1
  end
  seen.size
end
