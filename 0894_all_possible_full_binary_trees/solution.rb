# LeetCode 0894 - All Possible Full Binary Trees
# https://leetcode.com/problems/all-possible-full-binary-trees/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

# @param {Integer} n
# @return {TreeNode[]}
def all_possible_fbt(n)
  memo = {}
  build = lambda do |nodes|
    return memo[nodes] if memo.key?(nodes)
    return memo[nodes] = [] if nodes.even?
    return memo[nodes] = [TreeNode.new(0)] if nodes == 1

    res = []
    (1...nodes).step(2) do |left|
      right = nodes - 1 - left
      build.call(left).each do |l|
        build.call(right).each do |r|
          root = TreeNode.new(0)
          root.left = l
          root.right = r
          res << root
        end
      end
    end
    memo[nodes] = res
  end

  to_list = lambda do |root|
    return [] if root.nil?

    result = []
    queue = [root]
    until queue.empty?
      node = queue.shift
      if node.nil?
        result << nil
        next
      end
      result << node.val
      queue << node.left
      queue << node.right
    end
    result.pop while !result.empty? && result.last.nil?
    result
  end

  build.call(n).map { |t| to_list.call(t) }
end
