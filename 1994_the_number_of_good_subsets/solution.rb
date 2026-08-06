# LeetCode 1994 - The Number of Good Subsets
# https://leetcode.com/problems/the-number-of-good-subsets/

# @param {Integer[]} nums
# @return {Integer}
def number_of_good_subsets(nums)
  mod = 10**9 + 7
  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
  masks = Array.new(31, 0)
  (2..30).each do |x|
    m = 0
    y = x
    ok = true
    primes.each_with_index do |p, i|
      next unless (y % p).zero?
      if ((y / p) % p).zero?
        ok = false
        break
      end
      m |= 1 << i
      y /= p
    end
    masks[x] = ok ? m : -1
  end

  cnt = Array.new(31, 0)
  nums.each { |v| cnt[v] += 1 }

  dp = Array.new(1 << primes.length, 0)
  dp[0] = 1
  (2..30).each do |x|
    next if cnt[x].zero? || masks[x] < 0
    m = masks[x]
    ((1 << primes.length) - 1).downto(0) do |state|
      next unless (state & m).zero?
      dp[state | m] = (dp[state | m] + dp[state] * cnt[x]) % mod
    end
  end

  ans = dp[1..].sum % mod
  ans * mod_pow(2, cnt[1], mod) % mod
end

def mod_pow(base, exp, mod)
  result = 1
  base %= mod
  while exp.positive?
    result = result * base % mod if exp.odd?
    base = base * base % mod
    exp /= 2
  end
  result
end
