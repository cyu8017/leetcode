"use strict";
// LeetCode 1563 - Stone Game V
// https://leetcode.com/problems/stone-game-v/
// @ts-nocheck
function stoneGameV(stoneValue) {
    const n = stoneValue.length;
    const pre = [0];
    for (const x of stoneValue)
        pre.push(pre[pre.length - 1] + x);
    const dp = Array.from({ length: n }, () => Array(n).fill(0));
    const left = Array.from({ length: n }, () => Array(n).fill(0));
    const right = Array.from({ length: n }, () => Array(n).fill(0));
    for (let i = 0; i < n; i++)
        left[i][i] = right[i][i] = stoneValue[i];
    for (let length = 2; length <= n; length++) {
        for (let i = 0; i <= n - length; i++) {
            const j = i + length - 1;
            let lo = i, hi = j - 1;
            while (lo <= hi) {
                const mid = (lo + hi) >> 1;
                if (2 * (pre[mid + 1] - pre[i]) >= pre[j + 1] - pre[i])
                    hi = mid - 1;
                else
                    lo = mid + 1;
            }
            const split = lo;
            const leftSum = pre[split + 1] - pre[i];
            const rightSum = pre[j + 1] - pre[split + 1];
            let best = right[split + 1][j];
            if (leftSum === rightSum)
                best = Math.max(best, left[i][split]);
            else if (split > i)
                best = Math.max(best, left[i][split - 1]);
            dp[i][j] = best;
            const total = pre[j + 1] - pre[i];
            left[i][j] = Math.max(left[i][j - 1], total + best);
            right[i][j] = Math.max(right[i + 1][j], total + best);
        }
    }
    return n ? dp[0][n - 1] : 0;
}
