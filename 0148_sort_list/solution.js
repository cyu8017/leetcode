// LeetCode 0148 - Sort List
// https://leetcode.com/problems/sort-list/

/**
 * @param {{ val: number, next: object|null }|null} head
 * @return {object|null}
 */
var sortList = function(head) {
  if (!head || !head.next) return head;

  let slow = head;
  let fast = head;
  let previous = null;
  while (fast && fast.next) {
    previous = slow;
    slow = slow.next;
    fast = fast.next.next;
  }
  previous.next = null;

  return merge(sortList(head), sortList(slow));
};

/**
 * @param {object|null} left
 * @param {object|null} right
 * @return {object|null}
 */
var merge = function(left, right) {
  const dummy = { val: 0, next: null };
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
};