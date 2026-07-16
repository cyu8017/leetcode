# LeetCode 0445 - Add Two Numbers II
# https://leetcode.com/problems/add-two-numbers-ii/

class ListNode
  attr_accessor :val, :next

  def initialize(val = 0, nxt = nil)
    @val = val
    @next = nxt
  end
end

class Solution
  def add_two_numbers(l1, l2)
    stack1 = []
    stack2 = []
    while l1
      stack1 << l1.val
      l1 = l1.next
    end
    while l2
      stack2 << l2.val
      l2 = l2.next
    end

    carry = 0
    head = nil
    while !stack1.empty? || !stack2.empty? || carry != 0
      total = carry
      total += stack1.pop unless stack1.empty?
      total += stack2.pop unless stack2.empty?
      carry, digit = total.divmod(10)
      node = ListNode.new(digit, head)
      head = node
    end
    head
  end

  alias_method :addTwoNumbers, :add_two_numbers
end
