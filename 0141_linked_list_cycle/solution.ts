// LeetCode 0141 - Linked List Cycle
// https://leetcode.com/problems/linked-list-cycle/

interface ListNode {
  val: number;
  next: ListNode | null;
}

export function hasCycle(head: ListNode | null): boolean {
  let slow = head;
  let fast = head;

  while (fast && fast.next) {
    slow = slow!.next;
    fast = fast.next.next;
    if (slow === fast) return true;
  }
  return false;
}