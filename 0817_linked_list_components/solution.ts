// LeetCode 0817 - Linked List Components
// https://leetcode.com/problems/linked-list-components/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

export function numComponents(head: ListNode | null, nums: number[]): number {
    const present = new Set(nums);
    let count = 0, connected = false;
    while (head) {
        if (present.has(head.val)) {
            if (!connected) {
                count++;
                connected = true;
            }
        } else {
            connected = false;
        }
        head = head.next;
    }
    return count;
}
