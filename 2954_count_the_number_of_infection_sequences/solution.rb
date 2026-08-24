# LeetCode 2954 - Count the Number of Infection Sequences
# https://leetcode.com/problems/count-the-number-of-infection-sequences/

MOD = 1_000_000_007

# @param {Integer} n
# @param {Integer[]} sick
# @return {Integer}
def number_of_sequence(n, sick)
  fact = Array.new(n + 1, 0)
  inv_fact = Array.new(n + 1, 0)
  fact[0] = 1
  (1..n).each { |i| fact[i] = fact[i - 1] * i % MOD }
  inv_fact[n] = mod_pow(fact[n], MOD - 2)
  n.downto(1) { |i| inv_fact[i - 1] = inv_fact[i] * i % MOD }
  m = sick.length
  total_empty = n - m
  ans = fact[total_empty]
  prev = -1
  sick.each do |s|
    gap = s - prev - 1
    if prev == -1
      ans = ans * inv_fact[gap] % MOD
    elsif gap > 0
      ans = ans * inv_fact[gap] % MOD * mod_pow(2, gap - 1) % MOD
    end
    prev = s
  end
  gap2 = n - prev - 1
  ans * inv_fact[gap2] % MOD
end

def mod_pow(a, b)
  res = 1
  a %= MOD
  while b > 0
    res = res * a % MOD if b.odd?
    a = a * a % MOD
    b >>= 1
  end
  res
end
