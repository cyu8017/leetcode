# LeetCode 1372 - Longest Zigzag Path In A Binary Tree
# https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/

def longest_zig_zag(root)
  ans = 0
  dfs = lambda do |node|
    return [-1, -1] if node.nil?
    l = dfs.call(node.left)
    r = dfs.call(node.right)
    a = l[1] + 1
    b = r[0] + 1
    ans = [ans, a, b].max
    [a, b]
  end
  dfs.call(root)
  ans
end
