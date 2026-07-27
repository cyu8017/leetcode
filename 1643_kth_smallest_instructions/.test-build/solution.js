"use strict";
// LeetCode 1643 - Kth Smallest Instructions
// https://leetcode.com/problems/kth-smallest-instructions/
function kthSmallestPath(destination, k) {
    let [v, h] = destination;
    const ans = [];
    const comb = (N, R) => {
        if (R < 0 || R > N)
            return 0;
        R = Math.min(R, N - R);
        let res = 1;
        for (let i = 0; i < R; i++) {
            res = res * (N - i) / (i + 1);
        }
        return Math.round(res);
    };
    while (h + v) {
        if (h) {
            const count = comb(h + v - 1, v);
            if (k <= count) {
                ans.push("H");
                h--;
                continue;
            }
            k -= count;
        }
        ans.push("V");
        v--;
    }
    return ans.join("");
}
