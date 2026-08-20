// LeetCode 1290 - Convert Binary Number in a Linked List to Integer
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val = 0, next: ListNode | null = null) {
        this.val = val;
        this.next = next;
    }
}

function getDecimalValue(head: ListNode | null): number {
    let value = 0;
    while (head) {
        value = value * 2 + head.val;
        head = head.next;
    }
    return value;
}
