# LeetCode 0919 - Complete Binary Tree Inserter
# https://leetcode.com/problems/complete-binary-tree-inserter/

class TreeNode
  attr_accessor :val, :left, :right

  def initialize(val = 0, left = nil, right = nil)
    @val = val
    @left = left
    @right = right
  end
end

class CBTInserter
  def initialize(root)
    root = self.class.list_to_tree(root) if root.is_a?(Array)
    @root = root
    @queue = []
    q = [root]
    until q.empty?
      node = q.shift
      if node.left
        q << node.left
      else
        @queue << node
        break
      end
      if node.right
        q << node.right
      else
        @queue << node
        break
      end
    end
    @queue.concat(q)
  end

  def insert(val)
    parent = @queue[0]
    child = TreeNode.new(val)
    if parent.left.nil?
      parent.left = child
    else
      parent.right = child
      @queue.shift
    end
    @queue << child
    parent.val
  end

  def get_root
    self.class.tree_to_list(@root)
  end

  def self.list_to_tree(values)
    return nil if values.nil? || values.empty?

    root = TreeNode.new(values[0])
    queue = [root]
    index = 1
    while !queue.empty? && index < values.length
      node = queue.shift
      if index < values.length
        unless values[index].nil?
          node.left = TreeNode.new(values[index])
          queue << node.left
        end
        index += 1
      end
      if index < values.length
        unless values[index].nil?
          node.right = TreeNode.new(values[index])
          queue << node.right
        end
        index += 1
      end
    end
    root
  end

  def self.tree_to_list(root)
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
end
