# LeetCode 3333 - Find the Original Typed String II
# https://leetcode.com/problems/find-the-original-typed-string-ii/

# @param {String} word
# @param {Integer} k
# @return {Integer}
def possible_string_count(word, k)
  mod = 1_000_000_007
  groups = []
  i = 0
  while i < word.length
    j = i
    j += 1 while j < word.length && word[j] == word[i]
    groups << (j - i)
    i = j
  end
  total = 1
  groups.each { |g| total = total * g % mod }
  return total if k <= groups.length

  need = k - 1
  dp = Array.new(need, 0)
  dp[0] = 1
  groups.each do |g|
    ndp = Array.new(need, 0)
    pref = Array.new(need + 1, 0)
    need.times { |ii| pref[ii + 1] = (pref[ii] + dp[ii]) % mod }
    need.times do |s|
      lo = s - g
      lo = 0 if lo < 0
      hi = s - 1
      ndp[s] = (pref[hi + 1] - pref[lo] + mod) % mod if hi >= 0
    end
    dp = ndp
  end
  bad = 0
  dp.each { |v| bad = (bad + v) % mod }
  (total - bad + mod) % mod
end
