# LeetCode 0437 - Path Sum III
# https://leetcode.com/problems/path-sum-iii/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class Solution
  def path_sum(root, target_sum)
    prefix_counts = Hash.new(0)
    prefix_counts[0] = 1
    dfs(root, 0, target_sum, prefix_counts)
  end

  alias_method :pathSum, :path_sum

  private

  def dfs(node, current, target_sum, prefix_counts)
    return 0 if node.nil?

    current += node.val
    total = prefix_counts[current - target_sum]
    prefix_counts[current] += 1
    total += dfs(node.left, current, target_sum, prefix_counts)
    total += dfs(node.right, current, target_sum, prefix_counts)
    prefix_counts[current] -= 1
    total
  end
end
