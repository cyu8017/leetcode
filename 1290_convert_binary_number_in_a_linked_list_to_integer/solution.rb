# LeetCode 1290 - Convert Binary Number in a Linked List to Integer
# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# @param {ListNode} head
# @return {Integer}
def get_decimal_value(head)
  value = 0
  while head
    value = value * 2 + head.val
    head = head.next
  end
  value
end
