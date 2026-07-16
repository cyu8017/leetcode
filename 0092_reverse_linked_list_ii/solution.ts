// LeetCode 0092 - Reverse Linked List II
// https://leetcode.com/problems/reverse-linked-list-ii/

class ListNode {
    val: number;
    next: ListNode | null;

    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
}

export function reverseBetween(
    head: ListNode | null,
    left: number,
    right: number
): ListNode | null {
    if (!head || left === right) {
        return head;
    }

    const dummy = new ListNode(0, head);
    let before: ListNode = dummy;
    for (let i = 0; i < left - 1; i++) {
        before = before.next!;
    }

    const start = before.next!;
    let current = start.next;

    for (let i = 0; i < right - left; i++) {
        start.next = current!.next;
        current!.next = before.next;
        before.next = current;
        current = start.next;
    }

    return dummy.next;
}
