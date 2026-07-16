// LeetCode 0019 - Remove Nth Node From End of List
// https://leetcode.com/problems/remove-nth-node-from-end-of-list/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

export function removeNthFromEnd(head: ListNode | null, n: number): ListNode | null {
    const dummy = new ListNode(0, head);
    let fast: ListNode | null = dummy;
    let slow: ListNode | null = dummy;

    for (let i = 0; i < n; i++) {
        fast = fast!.next;
    }

    while (fast!.next) {
        fast = fast!.next;
        slow = slow!.next;
    }

    slow!.next = slow!.next!.next;
    return dummy.next;
}
