# LeetCode 3292 - Minimum Number of Valid Strings to Form Target II
# https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/

# @param {String[]} words
# @param {String} target
# @return {Integer}
def min_valid_strings(words, target)
  n = target.length
  inf = 1_000_000_000
  dp = Array.new(n + 1, inf)
  dp[0] = 0
  root = { next: Array.new(26) }
  words.each do |w|
    cur = root
    w.each_char do |c|
      ci = c.ord - 97
      cur[:next][ci] ||= { next: Array.new(26) }
      cur = cur[:next][ci]
    end
  end
  n.times do |i|
    next if dp[i] == inf

    cur = root
    (i...n).each do |j|
      ci = target[j].ord - 97
      break unless cur[:next][ci]

      cur = cur[:next][ci]
      dp[j + 1] = dp[i] + 1 if dp[i] + 1 < dp[j + 1]
    end
  end
  dp[n] == inf ? -1 : dp[n]
end
