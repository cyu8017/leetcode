# LeetCode 1602 - Find Nearest Right Node in Binary Tree
# https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/

# @param {TreeNode} root
# @param {TreeNode|Integer} u
# @return {TreeNode|Integer|nil}
def find_nearest_right_node(root, u)
  as_node = u.respond_to?(:val)
  target = as_node ? u.val : u
  q = root ? [root] : []
  while !q.empty?
    nxt = []
    q.each_with_index do |node, i|
      if node.val == target
        ans = i + 1 < q.length ? q[i + 1] : nil
        return as_node ? ans : (ans ? ans.val : nil)
      end
      nxt << node.left if node.left
      nxt << node.right if node.right
    end
    q = nxt
  end
  nil
end
