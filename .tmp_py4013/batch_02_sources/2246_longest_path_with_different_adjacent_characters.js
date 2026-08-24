// LeetCode 2246 - Longest Path With Different Adjacent Characters
// https://leetcode.com/problems/longest-path-with-different-adjacent-characters/

/**
 * @param {number[]} parent
 * @param {string} s
 * @return {number}
 */
var longestPath = function(parent, s) {
    const n = parent.length;
    const g = Array.from({length: n}, () => []);
    for (let i = 1; i < n; i++) g[parent[i]].push(i);
    let ans = 1;
    function dfs(u) {
        let best1 = 0, best2 = 0;
        for (const v of g[u]) {
            const len = dfs(v);
            if (s[v] === s[u]) continue;
            if (len > best1) { best2 = best1; best1 = len; }
            else if (len > best2) best2 = len;
        }
        ans = Math.max(ans, 1 + best1 + best2);
        return 1 + best1;
    }
    dfs(0);
    return ans;
};
