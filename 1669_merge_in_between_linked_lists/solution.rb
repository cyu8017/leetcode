# LeetCode 1669 - Merge In Between Linked Lists
# https://leetcode.com/problems/merge-in-between-linked-lists/

# @param {ListNode} list1
# @param {Integer} a
# @param {Integer} b
# @param {ListNode} list2
# @return {ListNode}
def merge_in_between(list1, a, b, list2)
  pre = list1
  (a - 1).times { pre = pre.next }
  post = pre
  (b - a + 2).times { post = post.next }
  pre.next = list2
  pre = pre.next while pre.next
  pre.next = post
  list1
end
