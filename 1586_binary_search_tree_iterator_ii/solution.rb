# LeetCode 1586 - Binary Search Tree Iterator II
# https://leetcode.com/problems/binary-search-tree-iterator-ii/

class BSTIterator
  def initialize(root)
    @values = []
    stack = []
    while !stack.empty? || root
      while root
        stack << root
        root = root.left
      end
      root = stack.pop
      @values << root.val
      root = root.right
    end
    @index = -1
  end

  def has_next
    @index + 1 < @values.length
  end

  def next
    @index += 1
    @values[@index]
  end

  def has_prev
    @index > 0
  end

  def prev
    @index -= 1
    @values[@index]
  end
end
