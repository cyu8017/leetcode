// LeetCode 0206 - Reverse Linked List
// https://leetcode.com/problems/reverse-linked-list/

export class ListNode {
    val: number;
    next: ListNode | null;

    constructor(val = 0, next: ListNode | null = null) {
        this.val = val;
        this.next = next;
    }
}

export function reverseList(head: ListNode | null): ListNode | null {
    let previous: ListNode | null = null;
    let current = head;
    while (current) {
        const next = current.next;
        current.next = previous;
        previous = current;
        current = next;
    }
    return previous;
}