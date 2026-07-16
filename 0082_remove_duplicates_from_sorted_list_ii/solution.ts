// LeetCode 0082 - Remove Duplicates from Sorted List II
// https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

export function deleteDuplicates(head: ListNode | null): ListNode | null {
    const dummy = new ListNode(0, head);
    let previous: ListNode = dummy;

    while (head) {
        if (head.next && head.val === head.next.val) {
            while (head.next && head.val === head.next.val) {
                head = head.next;
            }
            previous.next = head.next;
        } else {
            previous = previous.next!;
        }
        head = head.next;
    }

    return dummy.next;
}
