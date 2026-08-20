"use strict";
// LeetCode 1377 - Frog Position After T Seconds
// https://leetcode.com/problems/frog-position-after-t-seconds/
function frogPosition(n, edges, t, target) {
    const g = Array.from({ length: n + 1 }, (), any), any;
    [];
    ;
    for (const [a, b] of edges) {
        g[a].push(b);
        g[b].push(a);
    }
    const dfs = (u, p, time, prob) => {
        const kids = g[u].filter((v) => v !== p);
        if (time === t || !kids.length)
            return u === target ? prob : 0;
        let sum = 0;
        for (const v of kids)
            sum += dfs(v, u, time + 1, prob / kids.length);
        return sum;
    };
    return dfs(1, 0, 0, 1.0);
}
