// LeetCode 2816 - Double a Number Represented as a Linked List
// https://leetcode.com/problems/double-a-number-represented-as-a-linked-list/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

export function doubleIt(head: ListNode | null): ListNode | null {
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
    let carry = 0, cur = head, prev = null;
    while (cur) {
        const val = cur.val * 2 + carry;
        cur.val = val % 10;
        carry = Math.floor(val / 10);
        prev = cur;
        cur = cur.next;
    }
    if (carry > 0) prev.next = new ListNode(carry);
    return rev(head);
}
