// LeetCode 3062 - Winner of the Linked List Game
// https://leetcode.com/problems/winner-of-the-linked-list-game/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

export function gameResult(head: ListNode | null): string {
    let odd = 0, even = 0;
    for (; head !== null; head = head.next.next) {
        const a = head.val, b = head.next.val;
        if (a < b) odd++;
        if (a > b) even++;
    }
    if (odd > even) return "Odd";
    if (odd < even) return "Even";
    return "Tie";
}
