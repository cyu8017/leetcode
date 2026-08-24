# LeetCode 3327 - Check DFS Strings Are Palindromes
# https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/

# @param {String} t
# @return {Boolean}
def palindrome_str?(t)
  i = 0
  j = t.length - 1
  while i < j
    return false if t[i] != t[j]

    i += 1
    j -= 1
  end
  true
end

# @param {Integer[]} parent
# @param {String} s
# @return {Boolean[]}
def find_answer(parent, s)
  n = parent.length
  g = Array.new(n) { [] }
  (1...n).each { |i| g[parent[i]] << i }
  ans = Array.new(n, false)
  dfs_str = lambda do |u|
    out = ""
    g[u].each { |v| out += dfs_str.call(v) }
    out += s[u]
    ans[u] = palindrome_str?(out)
    out
  end
  dfs_str.call(0)
  ans
end
