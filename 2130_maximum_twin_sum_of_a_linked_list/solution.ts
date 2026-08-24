// LeetCode 2130 - Maximum Twin Sum of a Linked List
// https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

export function pairSum(head: ListNode | null): number {
    let slow = head, fast = head;
    while (fast !== null && fast.next !== null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    let prev = null;
    while (slow !== null) {
        const nxt = slow.next;
        slow.next = prev;
        prev = slow;
        slow = nxt;
    }
    let ans = 0;
    let a = head, b = prev;
    while (b !== null) {
        ans = Math.max(ans, a.val + b.val);
        a = a.next;
        b = b.next;
    }
    return ans;
}
