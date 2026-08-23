// LeetCode 2049 - Count Nodes With the Highest Score
// https://leetcode.com/problems/count-nodes-with-the-highest-score/

/**
 * @param {number[]} parents
 * @return {number}
 */
var countHighestScoreNodes = function(parents) {
    const n = parents.length;
    const children = Array.from({length: n}, () => []);
    for (let i = 1; i < n; i++) children[parents[i]].push(i);
    const size = new Array(n);
    const dfs = (u) => {
        size[u] = 1;
        for (const v of children[u]) size[u] += dfs(v);
        return size[u];
    };
    dfs(0);
    let best = 0, ans = 0;
    for (let u = 0; u < n; u++) {
        let score = 1;
        for (const v of children[u]) score *= size[v];
        const up = n - size[u];
        if (up > 0) score *= up;
        if (score > best) { best = score; ans = 1; }
        else if (score === best) ans++;
    }
    return ans;
};
