# LeetCode 2246 - Longest Path With Different Adjacent Characters
# https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

# @param {Integer[]} parent
# @param {String} s
# @return {Integer}
def longest_path(parent, s)
  n = parent.length
  g = Array.new(n) { [] }
  (1...n).each { |i| g[parent[i]] << i }
  ans = 1
  dfs = lambda do |u|
    best1 = best2 = 0
    g[u].each do |v|
      length = dfs.call(v)
      next if s[v] == s[u]

      if length > best1
        best2 = best1
        best1 = length
      elsif length > best2
        best2 = length
      end
    end
    ans = [ans, 1 + best1 + best2].max
    1 + best1
  end
  dfs.call(0)
  ans
end
