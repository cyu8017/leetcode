# LeetCode 0536 - Construct Binary Tree from String
# https://leetcode.com/problems/construct-binary-tree-from-string/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class Solution
  def str2tree(s)
    return nil if s.nil? || s.empty?

    index = 0
    parse = lambda do
      return nil if index >= s.length

      sign = 1
      if s[index] == "-"
        sign = -1
        index += 1
      end

      value = 0
      while index < s.length && s[index] >= "0" && s[index] <= "9"
        value = value * 10 + s[index].ord - "0".ord
        index += 1
      end

      node = TreeNode.new(sign * value)

      if index < s.length && s[index] == "("
        index += 1
        node.left = parse.call
        index += 1
      end

      if index < s.length && s[index] == "("
        index += 1
        node.right = parse.call
        index += 1
      end

      node
    end

    parse.call
  end
end
