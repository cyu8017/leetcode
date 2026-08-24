# LeetCode 3563 - Lexicographically Smallest String After Adjacent Removals
# https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/

# @param {String} s
# @return {String}
def lexicographically_smallest_string(s)
  is_consec = lambda do |a, b|
    d = (a.ord - b.ord).abs
    d == 1 || d == 25
  end
  n = s.length
  dp = Array.new(n + 1) { Array.new(n + 1, "") }
  (1..n).each do |length|
    (0..(n - length)).each do |i|
      j = i + length
      min_str = s[i] + dp[i + 1][j]
      ((i + 1)...j).each do |k|
        if is_consec.call(s[i], s[k]) && dp[i + 1][k] == ""
          cand = dp[k + 1][j]
          min_str = cand if cand < min_str
        end
      end
      dp[i][j] = min_str
    end
  end
  dp[0][n]
end
