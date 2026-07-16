// LeetCode 0062 - Unique Paths
// https://leetcode.com/problems/unique-paths/

export function uniquePaths(m: number, n: number): number {
    const row = new Array<number>(n).fill(1);

    for (let r = 1; r < m; r++) {
        for (let col = 1; col < n; col++) {
            row[col] += row[col - 1];
        }
    }

    return row[n - 1];
}
