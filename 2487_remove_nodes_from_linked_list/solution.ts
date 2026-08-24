// LeetCode 2487 - Remove Nodes From Linked List
// https://leetcode.com/problems/remove-nodes-from-linked-list/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

export function removeNodes(head: ListNode | null): ListNode | null {
    const rev = (node) => {
        let prev = null;
        while (node) {
            const nxt = node.next;
            node.next = prev;
            prev = node;
            node = nxt;
        }
        return prev;
    };
    head = rev(head);
    let mx = 0;
    const dummy = new ListNode(0, head);
    let prev = dummy;
    while (prev.next) {
        if (prev.next.val >= mx) {
            mx = prev.next.val;
            prev = prev.next;
        } else {
            prev.next = prev.next.next;
        }
    }
    return rev(dummy.next);
}
