# LeetCode 3981 - Count Distinct Ways to Form Target from Two Strings
# https://leetcode.com/problems/count-distinct-ways-to-form-target-from-two-strings/

# @param {String} word1
# @param {String} word2
# @param {String} target
# @return {Integer}
def count_ways(word1, word2, target)
  index = lambda { |i, j, mask, n2| ((i * (n2 + 1) + j) * 4) + mask }
  mod = 1_000_000_007
  n1 = word1.length
  n2 = word2.length
  size = (n1 + 1) * (n2 + 1) * 4
  dp = Array.new(size, 0)
  dp[index.call(0, 0, 0, n2)] = 1
  target.each_char do |ch|
    nxt = Array.new(size, 0)
    (0..n2).each do |j|
      prefix = Array.new(4, 0)
      n1.times do |a|
        4.times do |mask|
          prefix[mask] += dp[index.call(a, j, mask, n2)]
          prefix[mask] -= mod if prefix[mask] >= mod
        end
        next unless word1[a] == ch
        4.times do |mask|
          at = index.call(a + 1, j, mask | 1, n2)
          nxt[at] += prefix[mask]
          nxt[at] -= mod if nxt[at] >= mod
        end
      end
    end
    (0..n1).each do |i|
      prefix = Array.new(4, 0)
      n2.times do |b|
        4.times do |mask|
          prefix[mask] += dp[index.call(i, b, mask, n2)]
          prefix[mask] -= mod if prefix[mask] >= mod
        end
        next unless word2[b] == ch
        4.times do |mask|
          at = index.call(i, b + 1, mask | 2, n2)
          nxt[at] += prefix[mask]
          nxt[at] -= mod if nxt[at] >= mod
        end
      end
    end
    dp = nxt
  end
  answer = 0
  (0..n1).each do |i|
    (0..n2).each do |j|
      answer += dp[index.call(i, j, 3, n2)]
      answer -= mod if answer >= mod
    end
  end
  answer
end
