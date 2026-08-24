// LeetCode 2181 - Merge Nodes in Between Zeros
// https://leetcode.com/problems/merge-nodes-in-between-zeros/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

export function mergeNodes(head: ListNode | null): ListNode | null {
    const dummy = new ListNode();
    let cur = dummy;
    let sum = 0;
    for (let p = head.next; p !== null; p = p.next) {
        if (p.val === 0) {
            cur.next = new ListNode(sum);
            cur = cur.next;
            sum = 0;
        } else sum += p.val;
    }
    return dummy.next;
}
