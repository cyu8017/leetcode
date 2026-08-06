# LeetCode 1516 - Move Sub-Tree of N-Ary Tree
# https://leetcode.com/problems/move-sub-tree-of-n-ary-tree/

# @param {Node} root
# @param {Node} p
# @param {Node} q
# @return {Node}
def move_sub_tree(root, p, q)
  parent = {}

  build = lambda do |node|
    node.children.each do |child|
      parent[child] = node
      build.call(child)
    end
  end
  build.call(root)

  return root if parent[p].equal?(q)

  is_ancestor = lambda do |a, b|
    cur = b
    while parent.key?(cur)
      cur = parent[cur]
      return true if cur.equal?(a)
    end
    false
  end

  p_parent = parent[p]
  q_parent = parent[q]

  if is_ancestor.call(p, q)
    q_parent.children.delete(q)
    if p_parent.nil?
      root = q
    else
      idx = p_parent.children.index(p)
      p_parent.children[idx] = q
    end
    q.children << p
  else
    if p_parent.nil?
      root = q
    else
      p_parent.children.delete(p)
    end
    q.children << p
  end
  root
end
