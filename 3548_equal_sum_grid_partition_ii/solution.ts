// LeetCode 3548 - Equal Sum Grid Partition II
// https://leetcode.com/problems/equal-sum-grid-partition-ii/

function rotate3548(grid: any): any {
    const m = grid.length, n = grid[0].length;
    const t = Array.from({length: n}, () => new Array(m));
    for (let i = 0; i < m; i++) for (let j = 0; j < n; j++) t[j][i] = grid[i][j];
    return t;
}function check3548(g: any): any {
    const m = g.length, n = g[0].length;
    let s1 = 0, s2 = 0;
    const cnt1 = new Map(), cnt2 = new Map();
    for (const row of g) for (const x of row) {
        s2 += x;
        cnt2.set(x, (cnt2.get(x) || 0) + 1);
    }
    for (let i = 0; i < m - 1; i++) {
        for (const x of g[i]) {
            s1 += x; s2 -= x;
            cnt1.set(x, (cnt1.get(x) || 0) + 1);
            cnt2.set(x, cnt2.get(x) - 1);
        }
        if (s1 === s2) return true;
        if (s1 < s2) {
            const diff = s2 - s1;
            if ((cnt2.get(diff) || 0) > 0) {
                if ((m - i - 1 > 1 && n > 1) ||
                    (i === m - 2 && (g[i + 1][0] === diff || g[i + 1][n - 1] === diff)) ||
                    (n === 1 && (g[i + 1][0] === diff || g[m - 1][0] === diff)))
                    return true;
            }
        } else {
            const diff = s1 - s2;
            if ((cnt1.get(diff) || 0) > 0) {
                if ((i + 1 > 1 && n > 1) ||
                    (i === 0 && (g[0][0] === diff || g[0][n - 1] === diff)) ||
                    (n === 1 && (g[0][0] === diff || g[i][0] === diff)))
                    return true;
            }
        }
    }
    return false;
}export function canPartitionGrid(grid: any): any {
    return check3548(grid) || check3548(rotate3548(grid));
}
