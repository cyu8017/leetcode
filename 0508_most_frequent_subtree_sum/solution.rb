# LeetCode 0508 - Most Frequent Subtree Sum
# https://leetcode.com/problems/most-frequent-subtree-sum/

class Solution
  def find_frequent_tree_sum(root)
    counts = Hash.new(0)

    subtree_sum = lambda do |node|
      return 0 if node.nil?

      total = node.val + subtree_sum.call(node.left) + subtree_sum.call(node.right)
      counts[total] += 1
      total
    end

    subtree_sum.call(root)
    return [] if counts.empty?

    best = counts.values.max
    counts.select { |_, count| count == best }.keys.sort
  end

  alias_method :findFrequentTreeSum, :find_frequent_tree_sum
end
