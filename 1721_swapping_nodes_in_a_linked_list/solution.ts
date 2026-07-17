// LeetCode 1721 - Swapping Nodes in a Linked List
// https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

function swapNodes(head: ListNode | null, k: number): ListNode | null {
    let first = head!;
    for (let i = 0; i < k - 1; i++) {
        first = first.next!;
    }
    let fast = first;
    let second = head!;
    while (fast.next) {
        fast = fast.next;
        second = second.next!;
    }
    const temp = first.val;
    first.val = second.val;
    second.val = temp;
    return head;
}
