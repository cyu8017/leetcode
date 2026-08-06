# LeetCode 1977 - Number of Ways to Separate Numbers
# https://leetcode.com/problems/number-of-ways-to-separate-numbers/

# @param {String} num
# @return {Integer}
def number_of_combinations(num)
  mod = 10**9 + 7
  n = num.length
  return 0 if num[0] == "0"

  lcp = Array.new(n + 1) { Array.new(n + 1, 0) }
  (n - 1).downto(0) do |i|
    (n - 1).downto(0) do |j|
      lcp[i][j] = lcp[i + 1][j + 1] + 1 if num[i] == num[j]
    end
  end

  le = lambda do |a, b, length|
    common = lcp[a][b]
    return true if common >= length
    num[a + common] < num[b + common]
  end

  dp = Array.new(n + 1) { Array.new(n + 1, 0) }
  pref = Array.new(n + 1) { Array.new(n + 1, 0) }

  (1..n).each do |i|
    (1..i).each do |l|
      start = i - l
      if num[start] == "0"
        dp[i][l] = 0
      elsif start.zero?
        dp[i][l] = 1
      else
        ways = l > 1 ? pref[start][[l - 1, start].min] : 0
        ways = (ways + dp[start][l]) % mod if start >= l && le.call(start - l, start, l)
        dp[i][l] = ways
      end
    end
    (1..n).each do |l|
      pref[i][l] = (pref[i][l - 1] + (l <= i ? dp[i][l] : 0)) % mod
    end
  end
  pref[n][n]
end
