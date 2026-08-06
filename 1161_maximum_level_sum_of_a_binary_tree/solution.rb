# LeetCode 1161 - Maximum Level Sum of a Binary Tree
# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

# @param {TreeNode} root
# @return {Integer}
def max_level_sum(root)
  queue = [root]
  best_sum = -Float::INFINITY
  best_level = level = 1
  until queue.empty?
    total = 0
    queue.length.times do
      node = queue.shift
      total += node.val
      queue << node.left if node.left
      queue << node.right if node.right
    end
    if total > best_sum
      best_sum = total
      best_level = level
    end
    level += 1
  end
  best_level
end
