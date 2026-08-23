// LeetCode 0851 - Loud and Rich
// https://leetcode.com/problems/loud-and-rich/

/**
 * @param {number[][]} richer
 * @param {number[]} quiet
 * @return {number[]}
 */
var loudAndRich = function(richer, quiet) {
    const n = quiet.length;
    const graph = Array.from({ length: n }, () => []);
    for (const [a, b] of richer) graph[b].push(a);
    const ans = new Array(n).fill(-1);
    const dfs = (person) => {
        if (ans[person] !== -1) return ans[person];
        let best = person;
        for (const richerPerson of graph[person]) {
            const cand = dfs(richerPerson);
            if (quiet[cand] < quiet[best]) best = cand;
        }
        ans[person] = best;
        return best;
    };
    for (let i = 0; i < n; i++) dfs(i);
    return ans;
};
