// LeetCode 3715 - Sum of Perfect Square Ancestors
// https://leetcode.com/problems/sum-of-perfect-square-ancestors/

export function sumOfAncestors(n: any, edges: any, nums: any): any {
    const graph = Array.from({length: n}, () => []);
    for (const e of edges) {
        graph[e[0]].push(e[1]);
        graph[e[1]].push(e[0]);
    }
    const kernel = (x) => {
        let res = 1;
        for (let p = 2; p * p <= x; p++) {
            let cnt = 0;
            while (x % p === 0) {
                x = Math.floor(x / p);
                cnt++;
            }
            if (cnt % 2 === 1) res *= p;
        }
        if (x > 1) res *= x;
        return res;
    };
    const ks = new Array(n);
    for (let i = 0; i < n; i++) ks[i] = kernel(nums[i]);
    const freq = new Map();
    let ans = 0;
    const dfs = (u, p) => {
        ans += freq.get(ks[u]) || 0;
        freq.set(ks[u], (freq.get(ks[u]) || 0) + 1);
        for (const v of graph[u]) if (v !== p) dfs(v, u);
        freq.set(ks[u], (freq.get(ks[u]) || 0) - 1);
    };
    dfs(0, -1);
    return ans;
}
