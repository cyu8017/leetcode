# LeetCode 3213 - Construct String with Minimum Cost
# https://leetcode.com/problems/construct-string-with-minimum-cost/

# @param {String} target
# @param {String[]} words
# @param {Integer[]} costs
# @return {Integer}
def minimum_cost(target, words, costs)
  bas = 13331
  mod = 998244353
  inf = 10**18
  n = target.length
  p = Array.new(n + 1, 0)
  h = Array.new(n + 1, 0)
  p[0] = 1
  (1..n).each do |i|
    p[i] = (p[i - 1] * bas) % mod
    h[i] = (h[i - 1] * bas + target[i - 1].ord) % mod
  end
  query = lambda do |l, r|
    (h[r] - (h[l - 1] * p[r - l + 1]) % mod + mod) % mod
  end
  f = Array.new(n + 1, inf)
  f[0] = 0
  lengths = words.map(&:length).uniq.sort
  d = {}
  words.each_with_index do |w, i|
    x = 0
    w.each_char { |ch| x = (x * bas + ch.ord) % mod }
    d[x] = costs[i] if !d.key?(x) || costs[i] < d[x]
  end
  (1..n).each do |i|
    lengths.each do |j|
      break if j > i
      x = query.call(i - j + 1, i)
      f[i] = [f[i], f[i - j] + d[x]].min if d.key?(x)
    end
  end
  f[n] >= inf ? -1 : f[n]
end
