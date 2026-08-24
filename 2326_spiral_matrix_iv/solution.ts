// LeetCode 2326 - Spiral Matrix IV
// https://leetcode.com/problems/spiral-matrix-iv/

class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

export function spiralMatrix(m: number, n: number, head: ListNode | null): number[][] {
    const ans = Array.from({ length: m }, () => Array(n).fill(-1));
    const dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]];
    let r = 0, c = 0, d = 0;
    while (head !== null) {
        ans[r][c] = head.val;
        head = head.next;
        let nr = r + dirs[d][0], nc = c + dirs[d][1];
        if (nr < 0 || nr >= m || nc < 0 || nc >= n || ans[nr][nc] !== -1) {
            d = (d + 1) % 4;
            nr = r + dirs[d][0];
            nc = c + dirs[d][1];
        }
        r = nr;
        c = nc;
    }
    return ans;
}
