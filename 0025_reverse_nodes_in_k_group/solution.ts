// LeetCode 0025 - Reverse Nodes in k-Group
// https://leetcode.com/problems/reverse-nodes-in-k-group/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

export function reverseKGroup(head: ListNode | null, k: number): ListNode | null {
    const dummy = new ListNode(0, head);
    let groupPrevious: ListNode = dummy;

    while (true) {
        let kth: ListNode | null = groupPrevious;
        for (let i = 0; i < k; i++) {
            kth = kth!.next;
            if (!kth) {
                return dummy.next;
            }
        }

        const groupNext = kth!.next;
        let previous: ListNode | null = groupNext;
        let current: ListNode | null = groupPrevious.next;

        while (current !== groupNext) {
            const next = current!.next;
            current!.next = previous;
            previous = current;
            current = next;
        }

        const tmp = groupPrevious.next!;
        groupPrevious.next = kth;
        groupPrevious = tmp;
    }
}
