// LeetCode 2479 - Maximum XOR of Two Non-Overlapping Subtrees
// https://leetcode.com/problems/maximum-xor-of-two-non-overlapping-subtrees/

export function maxXor(n: number, edges: number[][], values: number[]): number {
    const g = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        g[a].push(b);
        g[b].push(a);
    }
    const sum = Array(n).fill(0);
    const dfsSum = (u, p) => {
        let s = values[u];
        for (const v of g[u]) if (v !== p) s += dfsSum(v, u);
        return (sum[u] = s);
    };
    dfsSum(0, -1);
    const root = { child: [null, null] };
    const insert = (x) => {
        let cur = root;
        for (let b = 46; b >= 0; b--) {
            const bit = Number((BigInt(x) >> BigInt(b)) & 1n);
            if (!cur.child[bit]) cur.child[bit] = { child: [null, null] };
            cur = cur.child[bit];
        }
    };
    const query = (x) => {
        let cur = root;
        if (!cur.child[0] && !cur.child[1]) return 0;
        let res = 0n;
        for (let b = 46; b >= 0; b--) {
            const bit = Number((BigInt(x) >> BigInt(b)) & 1n);
            const want = bit ^ 1;
            if (cur.child[want]) {
                res |= 1n << BigInt(b);
                cur = cur.child[want];
            } else if (cur.child[bit]) {
                cur = cur.child[bit];
            } else {
                return Number(res);
            }
        }
        return Number(res);
    };
    let ans = 0;
    const dfs = (u, p) => {
        for (const v of g[u]) {
            if (v === p) continue;
            const xorv = query(sum[v]);
            if (xorv > ans) ans = xorv;
            dfs(v, u);
            insert(sum[v]);
        }
    };
    dfs(0, -1);
    return ans;
}
