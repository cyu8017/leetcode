# LeetCode 1214 - Two Sum BSTs
# https://leetcode.com/problems/two-sum-bsts/

require "set"

# @param {TreeNode} root1
# @param {TreeNode} root2
# @param {Integer} target
# @return {Boolean}
def two_sum_bs_ts(root1, root2, target)
  values = Set.new
  stack = root1 ? [root1] : []
  until stack.empty?
    node = stack.pop
    values.add(node.val)
    stack << node.left if node.left
    stack << node.right if node.right
  end
  stack = root2 ? [root2] : []
  until stack.empty?
    node = stack.pop
    return true if values.include?(target - node.val)
    stack << node.left if node.left
    stack << node.right if node.right
  end
  false
end
