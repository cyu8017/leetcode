# LeetCode 3031 - Minimum Time to Revert Word to Initial State II
# https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/

class Hashing
  def initialize(word, bas, mod)
    @mod = mod
    n = word.length
    @p = Array.new(n + 1, 0)
    @h = Array.new(n + 1, 0)
    @p[0] = 1
    @h[0] = 0
    (1..n).each do |i|
      @p[i] = @p[i - 1] * bas % mod
      @h[i] = (@h[i - 1] * bas + (word[i - 1].ord - 97)) % mod
    end
  end

  def query(l, r)
    (@h[r] - @h[l - 1] * @p[r - l + 1] % @mod + @mod) % @mod
  end
end

# @param {String} word
# @param {Integer} k
# @return {Integer}
def minimum_time_to_initial_state(word, k)
  hashing = Hashing.new(word, 13331, 998_244_353)
  n = word.length
  i = k
  while i < n
    return i / k if hashing.query(1, n - i) == hashing.query(i + 1, n)

    i += k
  end
  (n + k - 1) / k
end
