// LeetCode 2807 - Insert Greatest Common Divisors in Linked List
// https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

export function insertGreatestCommonDivisors(head: ListNode | null): ListNode | null {
    const gcd = (a, b) => {
        while (b) { const t = a % b; a = b; b = t; }
        return a;
    };
    let cur = head;
    while (cur && cur.next) {
        const g = gcd(cur.val, cur.next.val);
        const node = new ListNode(g, cur.next);
        cur.next = node;
        cur = node.next;
    }
    return head;
}
