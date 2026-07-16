# LeetCode 0428 - Serialize and Deserialize N-ary Tree
# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

class Node
  attr_accessor :val, :children

  def initialize(val = nil, children = nil)
    @val = val
    @children = children || []
  end
end

class Codec
  def encode(root)
    return "" if root.nil?

    parts = []
    queue = [root]
    until queue.empty?
      node = queue.shift
      parts << node.val.to_s
      parts << node.children.length.to_s
      node.children.each do |child|
        parts << child.val.to_s
        queue << child
      end
    end
    parts.join(",")
  end

  def decode(data)
    return nil if data.nil? || data.empty?

    values = data.split(",")
    index = 0

    read_root = lambda do
      value = values[index].to_i
      child_count = values[index + 1].to_i
      index += 2
      node = Node.new(value, [])
      child_count.times do
        node.children << Node.new(values[index].to_i, [])
        index += 1
      end
      node
    end

    root = read_root.call
    queue = root.children.dup
    until queue.empty?
      node = queue.shift
      value = values[index].to_i
      child_count = values[index + 1].to_i
      index += 2
      child_count.times do
        child = Node.new(values[index].to_i, [])
        node.children << child
        queue << child
        index += 1
      end
    end
    root
  end

  alias_method :serialize, :encode
  alias_method :deserialize, :decode
end
