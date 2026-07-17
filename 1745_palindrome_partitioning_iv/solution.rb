# LeetCode 1745 - Palindrome Partitioning IV
# https://leetcode.com/problems/palindrome-partitioning-iv/

# @param {String} s
# @return {Boolean}
def check_partitioning(s)
  n = s.length
  pal = Array.new(n) { Array.new(n, false) }
  (n - 1).downto(0) do |i|
    (i...n).each do |j|
      pal[i][j] = s[i] == s[j] && (j - i < 2 || pal[i + 1][j - 1])
    end
  end
  (0...n - 2).each do |i|
    (i + 1...n - 1).each do |j|
      return true if pal[0][i] && pal[i + 1][j] && pal[j + 1][n - 1]
    end
  end
  false
end
