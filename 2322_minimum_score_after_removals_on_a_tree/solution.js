// LeetCode 2322 - Minimum Score After Removals on a Tree
// https://leetcode.com/problems/minimum-score-after-removals-on-a-tree/

/**
 * @param {number[]} nums
 * @param {number[][]} edges
 * @return {number}
 */
var minimumScore = function(nums, edges) {
    const n = nums.length;
    const g = Array.from({ length: n }, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    const xorv = Array(n).fill(0);
    const inT = Array(n).fill(0);
    const outT = Array(n).fill(0);
    let time = 0;
    const dfs = (u, p) => {
        inT[u] = time++;
        xorv[u] = nums[u];
        for (const v of g[u]) if (v !== p) {
            dfs(v, u);
            xorv[u] ^= xorv[v];
        }
        outT[u] = time;
    };
    const isAncestor = (a, b) => inT[a] <= inT[b] && outT[b] <= outT[a];
    dfs(0, -1);
    const total = xorv[0];
    let ans = Infinity;
    for (let i = 1; i < n; ++i) {
        for (let j = i + 1; j < n; ++j) {
            let a, b, c;
            if (isAncestor(i, j)) {
                a = xorv[j];
                b = xorv[i] ^ xorv[j];
                c = total ^ xorv[i];
            } else if (isAncestor(j, i)) {
                a = xorv[i];
                b = xorv[j] ^ xorv[i];
                c = total ^ xorv[j];
            } else {
                a = xorv[i];
                b = xorv[j];
                c = total ^ xorv[i] ^ xorv[j];
            }
            const mx = Math.max(a, Math.max(b, c));
            const mn = Math.min(a, Math.min(b, c));
            ans = Math.min(ans, mx - mn);
        }
    }
    return ans;
};
