# LeetCode 1609 - Even Odd Tree
# https://leetcode.com/problems/even-odd-tree/

# @param {TreeNode} root
# @return {Boolean}
def is_even_odd_tree(root)
  q = [root]
  level = 0
  while !q.empty?
    prev = level.even? ? -Float::INFINITY : Float::INFINITY
    nxt = []
    q.each do |node|
      return false if node.val.even? == level.even?
      return false if level.even? && node.val <= prev
      return false if level.odd? && node.val >= prev

      prev = node.val
      nxt << node.left if node.left
      nxt << node.right if node.right
    end
    q = nxt
    level += 1
  end
  true
end
