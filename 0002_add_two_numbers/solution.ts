// LeetCode 0002 - Add Two Numbers
// https://leetcode.com/problems/add-two-numbers/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

function addTwoNumbers(l1: ListNode | null, l2: ListNode | null): ListNode | null {
    const dummy = new ListNode();
    let current: ListNode = dummy;
    let carry = 0;

    while (l1 || l2 || carry) {
        let total = carry;
        if (l1) {
            total += l1.val;
            l1 = l1.next;
        }
        if (l2) {
            total += l2.val;
            l2 = l2.next;
        }
        carry = Math.floor(total / 10);
        current.next = new ListNode(total % 10);
        current = current.next;
    }

    return dummy.next;
}
