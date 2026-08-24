// LeetCode 3063 - Linked List Frequency
// https://leetcode.com/problems/linked-list-frequency/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

export function frequenciesOfElements(head: ListNode | null): ListNode | null {
    const cnt = new Map();
    for (; head !== null; head = head.next)
        cnt.set(head.val, (cnt.get(head.val) || 0) + 1);
    let dummy = { val: 0, next: null };
    for (const val of cnt.values())
        dummy.next = { val, next: dummy.next };
    return dummy.next;
}
