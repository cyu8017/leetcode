// LeetCode 2058 - Find the Minimum and Maximum Number of Nodes Between Critical Points
// https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

export function nodesBetweenCriticalPoints(head: ListNode | null): number[] {
    const crit = [];
    let prev = head, cur = head.next, idx = 1;
    while (cur && cur.next) {
        if ((cur.val > prev.val && cur.val > cur.next.val) ||
            (cur.val < prev.val && cur.val < cur.next.val))
            crit.push(idx);
        prev = cur; cur = cur.next; idx++;
    }
    if (crit.length < 2) return [-1, -1];
    let mn = crit[1] - crit[0];
    for (let i = 2; i < crit.length; i++) mn = Math.min(mn, crit[i] - crit[i - 1]);
    return [mn, crit[crit.length - 1] - crit[0]];
}
