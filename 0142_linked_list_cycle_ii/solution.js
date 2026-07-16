// LeetCode 0142 - Linked List Cycle II
// https://leetcode.com/problems/linked-list-cycle-ii/

/**
 * @param {{ val: number, next: object|null }|null} head
 * @return {object|null}
 */
var detectCycle = function(head) {
  let slow = head;
  let fast = head;

  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) {
      slow = head;
      while (slow !== fast) {
        slow = slow.next;
        fast = fast.next;
      }
      return slow;
    }
  }
  return null;
};