# LeetCode 0369 - Plus One Linked List
# https://leetcode.com/problems/plus-one-linked-list/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next_node = nil)
    @val = val
    @next = next_node
  end
end

class Solution
  def plus_one(head)
    sentinel = ListNode.new(0, head)
    not_nine = sentinel
    node = head

    while node
      not_nine = node if node.val != 9
      node = node.next
    end

    not_nine.val += 1
    node = not_nine.next
    while node
      node.val = 0
      node = node.next
    end

    sentinel.val == 1 ? sentinel : sentinel.next
  end

  alias_method :plusOne, :plus_one
end
