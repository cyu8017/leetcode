// LeetCode 0024 - Swap Nodes in Pairs
// https://leetcode.com/problems/swap-nodes-in-pairs/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

export function swapPairs(head: ListNode | null): ListNode | null {
    const dummy = new ListNode(0, head);
    let previous: ListNode = dummy;

    while (previous.next && previous.next.next) {
        const first = previous.next;
        const second = previous.next.next;
        first.next = second.next;
        second.next = first;
        previous.next = second;
        previous = first;
    }

    return dummy.next;
}
