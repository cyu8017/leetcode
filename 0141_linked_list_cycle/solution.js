// LeetCode 0141 - Linked List Cycle
// https://leetcode.com/problems/linked-list-cycle/

/**
 * @param {{ val: number, next: object|null }|null} head
 * @return {boolean}
 */
var hasCycle = function(head) {
  let slow = head;
  let fast = head;

  while (fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if (slow === fast) return true;
  }
  return false;
};