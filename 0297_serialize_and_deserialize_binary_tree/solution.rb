# LeetCode 0297 - Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class Codec
  def serialize(root)
    return "" if root.nil?

    values = []
    queue = [root]
    until queue.empty?
      node = queue.shift
      if node.nil?
        values << ""
      else
        values << node.val.to_s
        queue << node.left
        queue << node.right
      end
    end
    values.pop while !values.empty? && values.last == ""
    values.join(",")
  end

  def deserialize(data)
    return nil if data.nil? || data.empty?

    values = data.split(",")
    root = TreeNode.new(values[0].to_i)
    queue = [root]
    index = 1
    until queue.empty? || index >= values.length
      node = queue.shift
      if index < values.length && !values[index].empty?
        node.left = TreeNode.new(values[index].to_i)
        queue << node.left
      end
      index += 1
      if index < values.length && !values[index].empty?
        node.right = TreeNode.new(values[index].to_i)
        queue << node.right
      end
      index += 1
    end
    root
  end
end
