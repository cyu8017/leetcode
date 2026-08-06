# LeetCode 1382 - Balance A Binary Search Tree
# https://leetcode.com/problems/balance-a-binary-search-tree/

def balance_bst(root)
  nodes = []
  walk = lambda do |x|
    return if x.nil?
    walk.call(x.left)
    nodes << x
    walk.call(x.right)
  end
  walk.call(root)
  build = lambda do |l, r|
    return nil if l >= r
    m = (l + r) / 2
    x = nodes[m]
    x.left = build.call(l, m)
    x.right = build.call(m + 1, r)
    x
  end
  build.call(0, nodes.length)
end
