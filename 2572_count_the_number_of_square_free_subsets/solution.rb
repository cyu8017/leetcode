# LeetCode 2572 - Count the Number of Square-Free Subsets
# https://leetcode.com/problems/count-the-number-of-square-free-subsets/

# @param {Integer[]} nums
# @return {Integer}
def square_free_subsets(nums)
  mod = 1_000_000_007
  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
  freq = Hash.new(0)
  nums.each { |x| freq[x] += 1 }

  mask_of = lambda do |x|
    mask = 0
    primes.each_with_index do |p, i|
      cnt = 0
      while x % p == 0
        x /= p
        cnt += 1
        return -1 if cnt > 1
      end
      mask |= 1 << i if cnt == 1
    end
    mask
  end

  dp = Array.new(1 << 10, 0)
  dp[0] = 1
  freq.each do |x, c|
    next if x == 1

    m = mask_of.call(x)
    next if m < 0

    ((1 << 10) - 1).downto(0) do |state|
      dp[state | m] = (dp[state | m] + dp[state] * c) % mod if (state & m) == 0
    end
  end
  ans = 0
  dp.each { |v| ans = (ans + v) % mod }
  ones = freq[1]
  mul = 1
  ones.times { mul = mul * 2 % mod }
  ans = ans * mul % mod
  (ans - 1 + mod) % mod
end
