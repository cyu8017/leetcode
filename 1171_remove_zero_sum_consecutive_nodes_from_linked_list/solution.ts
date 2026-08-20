// LeetCode 1171 - Remove Zero Sum Consecutive Nodes from Linked List
// https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val = 0, next: ListNode | null = null) {
        this.val = val;
        this.next = next;
    }
}

function removeZeroSumSublists(head: ListNode | null): ListNode {
    const dummy = { val: 0, next: head };
    let prefix = 0;
    const seen = new Map([[0, dummy]]);
    let node = dummy;
    while (node) {
        prefix += node.val;
        seen.set(prefix, node);
        node = node.next;
    }
    prefix = 0;
    node = dummy;
    while (node) {
        prefix += node.val;
        node.next = seen.get(prefix).next;
        node = node.next;
    }
    return dummy.next;
}
