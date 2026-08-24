// LeetCode 2326 - Spiral Matrix IV
// https://leetcode.com/problems/spiral-matrix-iv/

/**
 * @param {number} m
 * @param {number} n
 * @param {ListNode} head
 * @return {number[][]}
 */
var spiralMatrix = function(m, n, head) {
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
};
