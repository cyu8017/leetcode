"use strict";
// LeetCode 1625 - Lexicographically Smallest String After Applying Operations
// https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/
function findLexSmallestString(s, a, b) {
    const seen = new Set([s]);
    const q = [s];
    let ans = s;
    for (const cur of q) {
        if (cur < ans)
            ans = cur;
        let add = "";
        for (let i = 0; i < cur.length; i++) {
            add += String((Number(cur[i]) + (i % 2 ? a : 0)) % 10);
        }
        const rot = cur.slice(-b) + cur.slice(0, -b);
        for (const nxt of [add, rot]) {
            if (!seen.has(nxt)) {
                seen.add(nxt);
                q.push(nxt);
            }
        }
    }
    return ans;
}
