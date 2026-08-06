# LeetCode 1265 - Print Immutable Linked List in Reverse
# https://leetcode.com/problems/print-immutable-linked-list-in-reverse/

# @param {ImmutableListNode} head
# @return {Void}
def print_linked_list_in_reverse(head)
  return if head.nil?
  print_linked_list_in_reverse(head.getNext)
  head.printValue
end
