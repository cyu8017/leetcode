# LeetCode 2573 - Find the String with LCP
# https://leetcode.com/problems/find-the-string-with-lcp/

# @param {Integer[][]} lcp
# @return {String}
def find_the_string(lcp)
  n = lcp.length
  s = Array.new(n, 0)
  c = 97
  n.times do |i|
    next if s[i] != 0
    return "" if c > 122

    s[i] = c
    (i + 1...n).each { |j| s[j] = c if lcp[i][j] > 0 }
    c += 1
  end
  (n - 1).downto(0) do |i|
    (n - 1).downto(0) do |j|
      v = 0
      if s[i] == s[j]
        v = 1
        v += lcp[i + 1][j + 1] if i + 1 < n && j + 1 < n
      end
      return "" if lcp[i][j] != v
    end
  end
  s.map(&:chr).join
end
