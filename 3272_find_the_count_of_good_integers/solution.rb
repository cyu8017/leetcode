# LeetCode 3272 - Find the Count of Good Integers
# https://leetcode.com/problems/find-the-count-of-good-integers/

# @param {Integer} n
# @param {Integer} k
# @return {Integer}
def count_good_integers(n, k)
  half = (n + 1) / 2
  start = 1
  (1...half).each { start *= 10 }
  last = start * 10
  seen = {}
  ans = 0
  fact = Array.new(n + 1, 0)
  fact[0] = 1
  (1..n).each { |i| fact[i] = fact[i - 1] * i }
  (start...last).each do |h|
    s = h.to_s
    pal = s.dup
    rev_start = s.length - 1
    rev_start -= 1 if n.odd?
    rev_start.downto(0) { |i| pal += s[i] }
    next if pal.to_i % k != 0
    chars = pal.chars.sort.join
    next if seen[chars]
    seen[chars] = true
    cnt = Array.new(10, 0)
    chars.each_char { |c| cnt[c.ord - 48] += 1 }
    total = fact[n]
    cnt.each { |c| total /= fact[c] }
    if cnt[0] > 0
      bad = fact[n - 1]
      cnt[0] -= 1
      cnt.each { |c| bad /= fact[c] }
      cnt[0] += 1
      total -= bad
    end
    ans += total
  end
  ans
end
