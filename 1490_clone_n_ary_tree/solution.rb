# LeetCode 1490 - Clone N Ary Tree
# https://leetcode.com/problems/clone-n-ary-tree/

def clone_tree(root)
  return nil if root.nil?
  copy = root.class.new(root.val, [])
  copy.children = root.children.map { |child| clone_tree(child) }
  copy
end
