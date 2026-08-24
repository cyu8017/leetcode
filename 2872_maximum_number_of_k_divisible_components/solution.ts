// LeetCode 2872 - Maximum Number of K-Divisible Components
// https://leetcode.com/problems/maximum-number-of-k-divisible-components/

export function maxKDivisibleComponents(n: number, edges: number[][], values: number[], k: number): number {
    const g = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) {
        g[a].push(b);
        g[b].push(a);
    }
    let ans = 0;
    const dfs = (u, p) => {
        let sum = values[u] % k;
        for (const v of g[u]) {
            if (v === p) continue;
            sum = (sum + dfs(v, u)) % k;
        }
        if (sum === 0) ans++;
        return sum;
    };
    dfs(0, -1);
    return ans;
}
