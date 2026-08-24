# LeetCode 3757 - Number of Effective Subsequences
# https://leetcode.com/problems/number-of-effective-subsequences/

# @param {Integer[]} nums
# @return {Integer}
def count_effective_subsequences(nums)
  pop_count = lambda do |x|
    c = 0
    while x != 0
      c += x & 1
      x >>= 1
    end
    c
  end
  mod = 1_000_000_007
  allv = 0
  nums.each { |x| allv |= x }
  bits = []
  (0...20).each { |b| bits << b if ((allv >> b) & 1) != 0 }
  m = bits.length
  freq = Array.new(1 << m, 0)
  nums.each do |x|
    mask = 0
    (0...m).each { |i| mask |= 1 << i if ((x >> bits[i]) & 1) != 0 }
    freq[mask] += 1
  end
  disjoint = freq.dup
  (0...m).each do |b|
    (0...(1 << m)).each do |mask|
      disjoint[mask] += disjoint[mask ^ (1 << b)] if ((mask >> b) & 1) != 0
    end
  end
  pow2 = Array.new(nums.length + 1, 0)
  pow2[0] = 1
  (1..nums.length).each { |i| pow2[i] = pow2[i - 1] * 2 % mod }
  ans = 0
  full = (1 << m) - 1
  (1..full).each do |s|
    ways = pow2[disjoint[full ^ s]]
    bc = pop_count.call(s)
    if bc.odd?
      ans += ways
      ans -= mod if ans >= mod
    else
      ans -= ways
      ans += mod if ans < 0
    end
  end
  ans
end
