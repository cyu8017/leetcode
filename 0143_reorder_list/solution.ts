// LeetCode 0143 - Reorder List
// https://leetcode.com/problems/reorder-list/

interface ListNode {
  val: number;
  next: ListNode | null;
}

export function reorderList(head: ListNode | null): void {
  if (!head || !head.next) return;

  let slow: ListNode = head;
  let fast: ListNode = head;
  while (fast.next && fast.next.next) {
    slow = slow.next!;
    fast = fast.next.next;
  }

  let second = slow.next;
  slow.next = null;
  let previous: ListNode | null = null;
  while (second) {
    const next = second.next;
    second.next = previous;
    previous = second;
    second = next;
  }

  let first: ListNode | null = head;
  second = previous;
  while (second) {
    const firstNext = first!.next;
    const secondNext = second.next;
    first!.next = second;
    second.next = firstNext;
    first = firstNext;
    second = secondNext;
  }
}