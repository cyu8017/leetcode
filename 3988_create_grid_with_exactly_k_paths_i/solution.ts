// LeetCode 3988 - Create Grid With Exactly K Paths I
// https://leetcode.com/problems/create-grid-with-exactly-k-paths-i/

export function createGrid(m: any, n: any, k: any): any {
    const cands = [];
    if (k === 1) cands.push(["."]);
    else if (k === 2) cands.push(["..", ".."]);
    else if (k === 3) {
        cands.push(["..", "..", ".."]);
        cands.push(["...", "..."]);
    } else if (k === 4) {
        cands.push(["..", "..", "..", ".."]);
        cands.push(["....", "...."]);
        cands.push(["..#", "...", "#.."]);
    }
    for (const pat of cands) {
        const pr = pat.length, pc = pat[0].length;
        if (pr > m || pc > n) continue;
        const result = new Array(m);
        for (let i = 0; i < m; i++) {
            result[i] = '#'.repeat(n);
        }
        for (let i = 0; i < pr; i++) {
            const row = result[i].split('');
            for (let j = 0; j < pc; j++) row[j] = pat[i][j];
            result[i] = row.join('');
        }
        for (let i = pr; i < m; i++) {
            const row = result[i].split('');
            row[pc - 1] = '.';
            result[i] = row.join('');
        }
        for (let j = pc; j < n; j++) {
            const row = result[m - 1].split('');
            row[j] = '.';
            result[m - 1] = row.join('');
        }
        return result;
    }
    return [];
}
