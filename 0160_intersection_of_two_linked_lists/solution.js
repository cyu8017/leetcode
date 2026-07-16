// LeetCode 0160 - Intersection of Two Linked Lists
// https://leetcode.com/problems/intersection-of-two-linked-lists/

/**
 * Finds the shared node of two singly linked lists.
 * @param {ListNode|null} headA
 * @param {ListNode|null} headB
 * @return {ListNode|null}
 */
var getIntersectionNode = function(headA, headB) {
    let pointerA = headA;
    let pointerB = headB;

    while (pointerA !== pointerB) {
        pointerA = pointerA === null ? headB : pointerA.next;
        pointerB = pointerB === null ? headA : pointerB.next;
    }

    return pointerA;
};