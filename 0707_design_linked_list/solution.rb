# LeetCode 0707 - Design Linked List
# https://leetcode.com/problems/design-linked-list/

class MyLinkedList
  class Node
    attr_accessor :val, :next

    def initialize(val = 0)
      @val = val
      @next = nil
    end
  end

  def initialize
    @dummy = Node.new
    @size = 0
  end

  def get(index)
    return -1 if index < 0 || index >= @size

    node = @dummy.next
    index.times { node = node.next }
    node.val
  end

  def add_at_head(val)
    add_at_index(0, val)
  end

  def add_at_tail(val)
    add_at_index(@size, val)
  end

  def add_at_index(index, val)
    return if index < 0 || index > @size

    prev = @dummy
    index.times { prev = prev.next }
    node = Node.new(val)
    node.next = prev.next
    prev.next = node
    @size += 1
    nil
  end

  def delete_at_index(index)
    return if index < 0 || index >= @size

    prev = @dummy
    index.times { prev = prev.next }
    prev.next = prev.next.next
    @size -= 1
    nil
  end
end
