// LeetCode 0147 - Insertion Sort List
// https://leetcode.com/problems/insertion-sort-list/

interface ListNode {
  val: number;
  next: ListNode | null;
}

export function insertionSortList(head: ListNode | null): ListNode | null {
  const dummy: ListNode = { val: 0, next: null };
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
}