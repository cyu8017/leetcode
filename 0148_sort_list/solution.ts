// LeetCode 0148 - Sort List
// https://leetcode.com/problems/sort-list/

interface ListNode {
  val: number;
  next: ListNode | null;
}

export function sortList(head: ListNode | null): ListNode | null {
  if (!head || !head.next) return head;

  let slow: ListNode = head;
  let fast: ListNode | null = head;
  let previous: ListNode | null = null;
  while (fast && fast.next) {
    previous = slow;
    slow = slow.next!;
    fast = fast.next.next;
  }
  previous!.next = null;

  return merge(sortList(head), sortList(slow));
}

function merge(left: ListNode | null, right: ListNode | null): ListNode | null {
  const dummy: ListNode = { val: 0, next: null };
  let tail = dummy;

  while (left && right) {
    if (left.val <= right.val) {
      tail.next = left;
      left = left.next;
    } else {
      tail.next = right;
      right = right.next;
    }
    tail = tail.next;
  }
  tail.next = left || right;
  return dummy.next;
}