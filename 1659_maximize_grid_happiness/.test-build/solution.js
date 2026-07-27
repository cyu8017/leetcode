"use strict";
// LeetCode 1659 - Maximize Grid Happiness
// https://leetcode.com/problems/maximize-grid-happiness/
function getMaxGridHappiness(m, n, introvertsCount, extrovertsCount) {
    const pair = (a, b) => {
        if (!a || !b)
            return 0;
        return (a === 1 ? -30 : 20) + (b === 1 ? -30 : 20);
    };
    const states = 3 ** n;
    const cells = [];
    const intro = [];
    const extro = [];
    const row = [];
    for (let s = 0; s < states; s++) {
        let x = s;
        const a = [];
        for (let i = 0; i < n; i++) {
            a.push(x % 3);
            x = Math.floor(x / 3);
        }
        cells.push(a);
        intro.push(a.filter((z) => z === 1).length);
        extro.push(a.filter((z) => z === 2).length);
        let val = 0;
        for (const z of a) {
            if (z === 1)
                val += 120;
            else if (z === 2)
                val += 40;
        }
        for (let j = 1; j < n; j++)
            val += pair(a[j - 1], a[j]);
        row.push(val);
    }
    const compat = Array.from({ length: states }, () => Array(states).fill(0));
    for (let a = 0; a < states; a++) {
        for (let b = 0; b < states; b++) {
            let s = 0;
            for (let j = 0; j < n; j++)
                s += pair(cells[a][j], cells[b][j]);
            compat[a][b] = s;
        }
    }
    const memo = new Map();
    const dp = (r, prev, i, e) => {
        if (r === m)
            return 0;
        const key = `${r},${prev},${i},${e}`;
        if (memo.has(key))
            return memo.get(key);
        let best = 0;
        for (let s = 0; s < states; s++) {
            if (intro[s] <= i && extro[s] <= e) {
                best = Math.max(best, row[s] + compat[prev][s] + dp(r + 1, s, i - intro[s], e - extro[s]));
            }
        }
        memo.set(key, best);
        return best;
    };
    return dp(0, 0, introvertsCount, extrovertsCount);
}
