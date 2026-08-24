// LeetCode 3241 - Time Taken to Mark All Nodes
// https://leetcode.com/problems/time-taken-to-mark-all-nodes/

var timeTaken = function(edges) {
    const n = edges.length + 1;
    const ans = new Array(n).fill(0);
    const tree = Array.from({length: n}, () => []);
    const dp = Array.from({length: n}, () => ({ top1: {node: 0, time: 0}, top2: {node: 0, time: 0} }));
    for (const e of edges) { tree[e[0]].push(e[1]); tree[e[1]].push(e[0]); }
    const getTime = (u) => u % 2 === 0 ? 2 : 1;
    const dfs = (u, prev) => {
        let t1 = {node: 0, time: 0}, t2 = {node: 0, time: 0};
        for (const v of tree[u]) {
            if (v === prev) continue;
            const t = dfs(v, u) + getTime(v);
            if (t >= t1.time) { t2 = t1; t1 = {node: v, time: t}; }
            else if (t > t2.time) t2 = {node: v, time: t};
        }
        dp[u].top1 = t1; dp[u].top2 = t2;
        return t1.time;
    };
    const reroot = (u, prev, maxTime) => {
        ans[u] = maxTime;
        if (dp[u].top1.time > ans[u]) ans[u] = dp[u].top1.time;
        for (const v of tree[u]) {
            if (v === prev) continue;
            let side = dp[u].top1.time;
            if (dp[u].top1.node === v) side = dp[u].top2.time;
            const newMax = Math.max(maxTime, side);
            reroot(v, u, getTime(u) + newMax);
        }
    };
    dfs(0, -1);
    reroot(0, -1, 0);
    return ans;
};
