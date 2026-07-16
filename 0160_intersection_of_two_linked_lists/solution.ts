// LeetCode 0160 - Intersection of Two Linked Lists
// https://leetcode.com/problems/intersection-of-two-linked-lists/

export interface ListNode {
    val: number;
    next: ListNode | null;
}

export function getIntersectionNode(
    headA: ListNode | null,
    headB: ListNode | null,
): ListNode | null {
    let pointerA = headA;
    let pointerB = headB;

    while (pointerA !== pointerB) {
        pointerA = pointerA === null ? headB : pointerA.next;
        pointerB = pointerB === null ? headA : pointerB.next;
    }

    return pointerA;
}