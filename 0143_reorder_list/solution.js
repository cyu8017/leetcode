// LeetCode 0143 - Reorder List
// https://leetcode.com/problems/reorder-list/

/**
 * @param {{ val: number, next: object|null }|null} head
 * @return {void}
 */
var reorderList = function(head) {
  if (!head || !head.next) return;

  let slow = head;
  let fast = head;
  while (fast.next && fast.next.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  let second = slow.next;
  slow.next = null;
  let previous = null;
  while (second) {
    const next = second.next;
    second.next = previous;
    previous = second;
    second = next;
  }

  let first = head;
  second = previous;
  while (second) {
    const firstNext = first.next;
    const secondNext = second.next;
    first.next = second;
    second.next = firstNext;
    first = firstNext;
    second = secondNext;
  }
};