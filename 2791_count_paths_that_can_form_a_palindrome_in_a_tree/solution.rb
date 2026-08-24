# LeetCode 2791 - Count Paths That Can Form a Palindrome in a Tree
# https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/

# @param {Integer[]} parent
# @param {String} s
# @return {Integer}
def count_palindrome_paths(parent, s)
  n = parent.length
  g = Array.new(n) { [] }
  (1...n).each { |i| g[parent[i]] << i }
  freq = Hash.new(0)
  freq[0] = 1
  ans = [0]
  dfs = lambda do |u, mask|
    g[u].each do |v|
      nm = mask ^ (1 << (s[v].ord - 97))
      ans[0] += freq[nm]
      (0...26).each { |b| ans[0] += freq[nm ^ (1 << b)] }
      freq[nm] += 1
      dfs.call(v, nm)
    end
  end
  dfs.call(0, 0)
  ans[0]
end
