# LeetCode 2514 - Count Anagrams
# https://leetcode.com/problems/count-anagrams/

# @param {String} s
# @return {Integer}
def count_anagrams(s)
  mod = 1_000_000_007

  mod_pow = lambda do |a, e|
    res = 1
    a %= mod
    while e > 0
      res = res * a % mod if (e & 1) != 0
      a = a * a % mod
      e >>= 1
    end
    res
  end

  words = s.strip.empty? ? [] : s.strip.split(/\s+/)
  max_n = 0
  words.each { |w| max_n = w.length if w.length > max_n }
  fact = Array.new(max_n + 1, 0)
  inv_fact = Array.new(max_n + 1, 0)
  fact[0] = 1
  (1..max_n).each { |i| fact[i] = fact[i - 1] * i % mod }
  inv_fact[max_n] = mod_pow.call(fact[max_n], mod - 2)
  max_n.downto(1) { |i| inv_fact[i - 1] = inv_fact[i] * i % mod }
  ans = 1
  words.each do |word|
    cnt = Array.new(26, 0)
    word.each_byte { |b| cnt[b - 97] += 1 }
    cur = fact[word.length]
    cnt.each { |c| cur = cur * inv_fact[c] % mod }
    ans = ans * cur % mod
  end
  ans
end
