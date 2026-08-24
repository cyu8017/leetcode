// LeetCode 2046 - Sort Linked List Already Sorted Using Absolute Values
// https://leetcode.com/problems/sort-linked-list-already-sorted-using-absolute-values/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

export function sortLinkedList(head: ListNode | null): ListNode | null {
    if (!head) return null;
    let prev = head, cur = head.next;
    while (cur) {
        if (cur.val < 0) {
            prev.next = cur.next;
            cur.next = head;
            head = cur;
            cur = prev.next;
        } else {
            prev = cur;
            cur = cur.next;
        }
    }
    return head;
}
