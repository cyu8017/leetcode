// LeetCode 0955 - Delete Columns to Make Sorted II
// https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

export function minDeletionSize(strs: string[]): number {
    const n = strs.length, m = strs[0].length;
    let deleted = 0;
    const sortedPair = new Array(n - 1).fill(false);
    for (let c = 0; c < m; c++) {
        let bad = false;
        for (let r = 0; r + 1 < n; r++) {
            if (!sortedPair[r] && strs[r][c] > strs[r + 1][c]) { bad = true; break; }
        }
        if (bad) { deleted++; continue; }
        for (let r = 0; r + 1 < n; r++)
            if (strs[r][c] < strs[r + 1][c]) sortedPair[r] = true;
    }
    return deleted;
}
