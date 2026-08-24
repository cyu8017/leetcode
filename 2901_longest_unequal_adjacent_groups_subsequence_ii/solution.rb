# LeetCode 2901 - Longest Unequal Adjacent Groups Subsequence II
# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-ii/

# @param {String[]} words
# @param {Integer[]} groups
# @return {String[]}
def get_words_in_longest_subsequence(words, groups)
  n = words.length
  dp = Array.new(n, 1)
  prev = Array.new(n, -1)

  hamming = lambda do |a, b|
    return 100 if a.length != b.length

    (0...a.length).count { |i| a[i] != b[i] }
  end

  best = 1
  best_i = 0
  (0...n).each do |i|
    (0...i).each do |j|
      if groups[i] != groups[j] && hamming.call(words[i], words[j]) == 1 && dp[j] + 1 >= dp[i]
        dp[i] = dp[j] + 1
        prev[i] = j
      end
    end
    if dp[i] >= best
      best = dp[i]
      best_i = i
    end
  end
  path = []
  i = best_i
  while i != -1
    path << words[i]
    i = prev[i]
  end
  path.reverse
end
