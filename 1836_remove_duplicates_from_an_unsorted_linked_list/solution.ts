// LeetCode 1836 - Remove Duplicates From an Unsorted Linked List
// https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

function deleteDuplicatesUnsorted(head: ListNode | null): ListNode | null {
    const counts = new Map<number, number>();
    let node = head;
    while (node) {
        counts.set(node.val, (counts.get(node.val) || 0) + 1);
        node = node.next;
    }
    const dummy = new ListNode(0, head);
    let prev = dummy;
    node = head;
    while (node) {
        if ((counts.get(node.val) || 0) > 1) {
            prev.next = node.next;
            node = node.next;
        } else {
            prev = node;
            node = node.next;
        }
    }
    return dummy.next;
}
