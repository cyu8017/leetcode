// LeetCode 0960 - Delete Columns to Make Sorted III
// https://leetcode.com/problems/delete-columns-to-make-sorted-iii/

export function minDeletionSize(strs: string[]): number {
    const m = strs[0].length;
    const dp = new Array(m).fill(1);
    for (let j = 0; j < m; j++) {
        for (let i = 0; i < j; i++) {
            let ok = true;
            for (const row of strs) {
                if (row[i] > row[j]) { ok = false; break; }
            }
            if (ok) dp[j] = Math.max(dp[j], dp[i] + 1);
        }
    }
    return m - Math.max(...dp);
}
