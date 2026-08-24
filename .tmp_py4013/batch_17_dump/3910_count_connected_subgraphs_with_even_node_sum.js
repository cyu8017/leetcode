// LeetCode 3910 - Count Connected Subgraphs With Even Node Sum
// https://leetcode.com/problems/count-connected-subgraphs-with-even-node-sum/

var evenSumSubgraphs = function(nums, edges) {
    const n = nums.length;
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    const m = (1 << n) - 1;
    let vis = 0;
    const dfs = (u) => {
        vis |= 1 << u;
        for (const v of g[u]) {
            if (((vis >> v) & 1) === 0) dfs(v);
        }
    };
    let ans = 0;
    for (let sub = 1; sub <= m; sub++) {
        let s = 0;
        for (let i = 0; i < n; i++) {
            if (((sub >> i) & 1) !== 0) s += nums[i];
        }
        if (s % 2 !== 0) continue;
        vis = m ^ sub;
        let start = 31 - Math.clz32(sub);
        if (sub === 0) start = 0;
        dfs(start);
        if (vis === m) ans++;
    }
    return ans;
};
