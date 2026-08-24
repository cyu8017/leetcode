// LeetCode 0725 - Split Linked List in Parts
// https://leetcode.com/problems/split-linked-list-in-parts/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

export function splitListToParts(head: ListNode | null, k: number): ListNode | null[] {
    let length = 0;
    for (let node = head; node !== null; node = node.next) length++;
    const partSize = Math.floor(length / k), extra = length % k;
    const result = new Array(k).fill(null);
    let current = head;
    for (let i = 0; i < k; i++) {
        result[i] = current;
        const size = partSize + (i < extra ? 1 : 0);
        for (let j = 0; j < size - 1 && current !== null; j++) current = current.next;
        if (current !== null) {
            const nxt = current.next;
            current.next = null;
            current = nxt;
        }
    }
    return result;
}
