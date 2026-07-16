# LeetCode 0430 - Flatten a Multilevel Doubly Linked List
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

class Node
  attr_accessor :val, :prev, :next, :child

  def initialize(val = 0, prev = nil, next_node = nil, child = nil)
    @val = val
    @prev = prev
    @next = next_node
    @child = child
  end
end

class Solution
  def flatten(head)
    current = head
    while current
      if current.child
        next_node = current.next
        child_head = flatten(current.child)
        current.next = child_head
        child_head.prev = current
        tail = child_head
        tail = tail.next while tail.next
        tail.next = next_node
        next_node.prev = tail if next_node
        current.child = nil
      end
      current = current.next
    end
    head
  end
end
