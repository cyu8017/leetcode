# LeetCode 0449 - Serialize and Deserialize BST
# https://leetcode.com/problems/serialize-and-deserialize-bst/

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
    parts = []

    preorder = lambda do |node|
      if node.nil?
        parts << "#"
      else
        parts << node.val.to_s
        preorder.call(node.left)
        preorder.call(node.right)
      end
    end

    preorder.call(root)
    parts.join(",")
  end

  def deserialize(data)
    return nil if data.nil? || data.empty?

    values = data.split(",").each
    build = lambda do
      token = values.next
      return nil if token == "#"

      node = TreeNode.new(token.to_i)
      node.left = build.call
      node.right = build.call
      node
    end

    build.call
  end
end
