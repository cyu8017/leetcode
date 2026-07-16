// LeetCode 0147 - Insertion Sort List
// https://leetcode.com/problems/insertion-sort-list/

/**
 * @param {{ val: number, next: object|null }|null} head
 * @return {object|null}
 */
var insertionSortList = function(head) {
  const dummy = { val: 0, next: null };
  let current = head;

  while (current) {
    let previous = dummy;
    while (previous.next && previous.next.val < current.val) {
      previous = previous.next;
    }
    const next = current.next;
    current.next = previous.next;
    previous.next = current;
    current = next;
  }

  return dummy.next;
};