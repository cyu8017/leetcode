# LeetCode 1367 - Linked List In Binary Tree
# https://leetcode.com/problems/linked-list-in-binary-tree/

def is_sub_path(head, root)
  match = lambda do |a, b|
    return true if a.nil?
    return false if b.nil? || a.val != b.val
    match.call(a.next, b.left) || match.call(a.next, b.right)
  end
  return false if root.nil?
  match.call(head, root) || is_sub_path(head, root.left) || is_sub_path(head, root.right)
end
