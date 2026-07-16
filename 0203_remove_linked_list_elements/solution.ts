// LeetCode 0203 - Remove Linked List Elements
// https://leetcode.com/problems/remove-linked-list-elements/

export class ListNode {
    val: number;
    next: ListNode | null;

    constructor(val = 0, next: ListNode | null = null) {
        this.val = val;
        this.next = next;
    }
}

export function removeElements(head: ListNode | null, val: number): ListNode | null {
    const dummy = new ListNode(0, head);
    let current = dummy;
    while (current.next) {
        if (current.next.val === val) {
            current.next = current.next.next;
        } else {
            current = current.next;
        }
    }
    return dummy.next;
}