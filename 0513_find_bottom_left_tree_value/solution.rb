# LeetCode 0513 - Find Bottom Left Tree Value
# https://leetcode.com/problems/find-bottom-left-tree-value/

class Solution
  def find_bottom_left_value(root)
    return 0 if root.nil?

    queue = [root]
    leftmost = root.val

    until queue.empty?
      level_size = queue.length
      level_size.times do |index|
        node = queue.shift
        leftmost = node.val if index.zero?
        queue << node.left if node.left
        queue << node.right if node.right
      end
    end

    leftmost
  end

  alias_method :findBottomLeftValue, :find_bottom_left_value
end
