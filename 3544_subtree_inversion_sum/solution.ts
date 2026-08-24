// LeetCode 3544 - Subtree Inversion Sum
// https://leetcode.com/problems/subtree-inversion-sum/

export function subtreeInversionSum(edges: any, nums: any, k: any): any {
    const n = edges.length + 1;
    const graph = Array.from({length: n}, () => []);
    for (const e of edges) {
        graph[e[0]].push(e[1]);
        graph[e[1]].push(e[0]);
    }
    const parent = new Array(n).fill(-1);
    const memo = new Map();
    function dp(u: any, steps: any, inv: any): any {
        const key = u + ',' + steps + ',' + inv;
        if (memo.has(key)) return memo.get(key);
        let num = nums[u];
        if (inv) num = -num;
        let negNum = -num;
        for (const v of graph[u]) {
            if (v === parent[u]) continue;
            parent[v] = u;
            let ns = steps + 1;
            if (ns > k) ns = k;
            num += dp(v, ns, inv);
            if (steps === k) negNum += dp(v, 1, !inv);
        }
        let res = num;
        if (steps === k && negNum > res) res = negNum;
        memo.set(key, res);
        return res;
    }    return dp(0, k, false);
}
