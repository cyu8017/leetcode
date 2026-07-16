// LeetCode 0142 - Linked List Cycle II
// https://leetcode.com/problems/linked-list-cycle-ii/

interface ListNode {
  val: number;
  next: ListNode | null;
}

export function detectCycle(head: ListNode | null): ListNode | null {
  let slow = head;
  let fast = head;

  while (fast && fast.next) {
    slow = slow!.next;
    fast = fast.next.next;
    if (slow === fast) {
      slow = head;
      while (slow !== fast) {
        slow = slow!.next;
        fast = fast!.next;
      }
      return slow;
    }
  }
  return null;
}