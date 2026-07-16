# LeetCode 0382 - Linked List Random Node
# https://leetcode.com/problems/linked-list-random-node/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

class Solution
  def initialize(head)
    head = build_list(head) if head.is_a?(Array)
    @nodes = []
    current = head
    while current
      @nodes << current
      current = current.next
    end
    srand(327)
  end

  def get_random
    @nodes.sample.val
  end

  alias_method :getRandom, :get_random

  private

  def build_list(values)
    return nil if values.nil? || values.empty?

    head = ListNode.new(values[0])
    current = head
    values[1..].each do |value|
      current.next = ListNode.new(value)
      current = current.next
    end
    head
  end
end
