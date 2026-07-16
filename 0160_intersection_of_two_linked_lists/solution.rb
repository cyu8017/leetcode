# LeetCode 0160 - Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, next_node = nil)
    @val = val
    @next = next_node
  end
end

class Solution
  def get_intersection_node(head_a, head_b)
    a = head_a
    b = head_b
    until a.equal?(b)
      a = a ? a.next : head_b
      b = b ? b.next : head_a
    end
    a
  end
end