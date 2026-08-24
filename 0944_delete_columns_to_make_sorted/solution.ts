// LeetCode 0944 - Delete Columns to Make Sorted
// https://leetcode.com/problems/delete-columns-to-make-sorted/

export function minDeletionSize(strs: string[]): number {
    let ans = 0;
    const m = strs[0].length, n = strs.length;
    for (let c = 0; c < m; c++) {
        for (let r = 0; r + 1 < n; r++) {
            if (strs[r][c] > strs[r + 1][c]) { ans++; break; }
        }
    }
    return ans;
}
