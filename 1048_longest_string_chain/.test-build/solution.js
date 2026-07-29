"use strict";
// LeetCode 1048 - Longest String Chain
// https://leetcode.com/problems/longest-string-chain/
function longestStrChain(words) {
    words.sort((a, b) => a.length - b.length);
    const dp = new Map();
    let ans = 1;
    for (const w of words) {
        let best = 1;
        for (let i = 0; i < w.length; i++) {
            const prev = w.slice(0, i) + w.slice(i + 1);
            if (dp.has(prev))
                best = Math.max(best, dp.get(prev) + 1);
        }
        dp.set(w, best);
        ans = Math.max(ans, best);
    }
    return ans;
}
