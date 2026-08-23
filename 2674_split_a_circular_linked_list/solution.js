// LeetCode 2674 - Split a Circular Linked List
// https://leetcode.com/problems/split-a-circular-linked-list/

var splitCircularLinkedList = function(list) {
    if (!list) return [null, null];
    let slow = list, fast = list;
    while (fast.next !== list && fast.next.next !== list) {
        slow = slow.next;
        fast = fast.next.next;
    }
    if (fast.next.next === list) fast = fast.next;
    const head2 = slow.next;
    slow.next = list;
    fast.next = head2;
    return [list, head2];
};
