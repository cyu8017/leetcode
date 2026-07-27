// LeetCode 1632 - Rank Transform of a Matrix
// https://leetcode.com/problems/rank-transform-of-a-matrix/

/**
 * @param {number[][]} matrix
 * @return {number[][]}
 */
var matrixRankTransform = function(matrix) {
    const m = matrix.length, n = matrix[0].length;
    const groups = new Map();
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const v = matrix[i][j];
            if (!groups.has(v)) groups.set(v, []);
            groups.get(v).push([i, j]);
        }
    }
    const rank = Array(m + n).fill(0);
    const ans = Array.from({ length: m }, () => Array(n).fill(0));
    const values = [...groups.keys()].sort((a, b) => a - b);
    for (const value of values) {
        const parent = new Map();
        const find = (x) => {
            if (!parent.has(x)) parent.set(x, x);
            if (parent.get(x) !== x) parent.set(x, find(parent.get(x)));
            return parent.get(x);
        };
        for (const [i, j] of groups.get(value)) {
            const a = find(i), b = find(m + j);
            parent.set(a, b);
        }
        const best = new Map();
        for (const [i, j] of groups.get(value)) {
            const root = find(i);
            best.set(root, Math.max(best.get(root) || 0, rank[i], rank[m + j]));
        }
        for (const [i, j] of groups.get(value)) {
            ans[i][j] = best.get(find(i)) + 1;
        }
        for (const [i, j] of groups.get(value)) {
            rank[i] = Math.max(rank[i], ans[i][j]);
            rank[m + j] = Math.max(rank[m + j], ans[i][j]);
        }
    }
    return ans;
};
