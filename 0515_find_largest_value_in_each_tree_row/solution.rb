# LeetCode 0515 - Find Largest Value in Each Tree Row
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/

class Solution
  def largest_values(root)
    return [] if root.nil?

    result = []
    queue = [root]

    until queue.empty?
      level_max = -Float::INFINITY
      queue.length.times do
        node = queue.shift
        level_max = [level_max, node.val].max
        queue << node.left if node.left
        queue << node.right if node.right
      end
      result << level_max
    end

    result
  end

  alias_method :largestValues, :largest_values
end
