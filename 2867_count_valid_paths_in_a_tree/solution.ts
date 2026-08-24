// LeetCode 2867 - Count Valid Paths in a Tree
// https://leetcode.com/problems/count-valid-paths-in-a-tree/

export function countPaths(n: number, edges: number[][]): number {
    const isPrime = Array(n + 1).fill(true);
    isPrime[0] = isPrime[1] = false;
    for (let i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j <= n; j += i) isPrime[j] = false;
        }
    }
    const g = Array.from({ length: n + 1 }, () => []);
    for (const [a, b] of edges) {
        g[a].push(b);
        g[b].push(a);
    }
    const dfs = (u, p) => {
        if (isPrime[u]) return 0;
        let sz = 1;
        for (const v of g[u]) if (v !== p) sz += dfs(v, u);
        return sz;
    };
    let ans = 0;
    for (let u = 1; u <= n; u++) {
        if (!isPrime[u]) continue;
        let total = 0;
        for (const v of g[u]) {
            const c = dfs(v, u);
            ans += c;
            ans += total * c;
            total += c;
        }
    }
    return ans;
}
