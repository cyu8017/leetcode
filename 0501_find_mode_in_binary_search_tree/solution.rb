# LeetCode 0501 - Find Mode in Binary Search Tree
# https://leetcode.com/problems/find-mode-in-binary-search-tree/

class Solution
  def find_mode(root)
    counts = {}
    best = [0]

    inorder = lambda do |node|
      return if node.nil?

      inorder.call(node.left)
      counts[node.val] = counts.fetch(node.val, 0) + 1
      best[0] = [best[0], counts[node.val]].max
      inorder.call(node.right)
    end

    inorder.call(root)
    counts.select { |_, count| count == best[0] }.keys
  end

  alias_method :findMode, :find_mode
end
