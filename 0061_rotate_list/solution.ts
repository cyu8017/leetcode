// LeetCode 0061 - Rotate List
// https://leetcode.com/problems/rotate-list/

class ListNode {
    val: number;
    next: ListNode | null;

    constructor(val?: number, next?: ListNode | null) {
        this.val = val === undefined ? 0 : val;
        this.next = next === undefined ? null : next;
    }
}

export function rotateRight(head: ListNode | null, k: number): ListNode | null {
    if (!head || !head.next) {
        return head;
    }

    let tail: ListNode = head;
    let length = 1;
    while (tail.next) {
        tail = tail.next;
        length += 1;
    }

    tail.next = head;
    k %= length;
    if (k === 0) {
        tail.next = null;
        return head;
    }

    const steps = length - k;
    let newTail: ListNode = head;
    for (let i = 0; i < steps - 1; i++) {
        newTail = newTail.next!;
    }

    const newHead = newTail.next;
    newTail.next = null;
    return newHead;
}
