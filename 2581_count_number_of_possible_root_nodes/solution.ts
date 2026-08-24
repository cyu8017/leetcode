// LeetCode 2581 - Count Number of Possible Root Nodes
// https://leetcode.com/problems/count-number-of-possible-root-nodes/

export function rootCount(edges: number[][], guesses: number[][], k: number): number {
    const n = edges.length + 1;
    const g = Array.from({ length: n }, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    const guessSet = new Set();
    const pack = (a, b) => a + ',' + b;
    for (const gu of guesses) guessSet.add(pack(gu[0], gu[1]));
    const dfs1 = (u, p) => {
        let cnt = 0;
        for (const v of g[u]) {
            if (v === p) continue;
            if (guessSet.has(pack(u, v))) cnt++;
            cnt += dfs1(v, u);
        }
        return cnt;
    };
    let ans = 0;
    const dfs2 = (u, p, cur) => {
        if (cur >= k) ans++;
        for (const v of g[u]) {
            if (v === p) continue;
            let nxt = cur;
            if (guessSet.has(pack(u, v))) nxt--;
            if (guessSet.has(pack(v, u))) nxt++;
            dfs2(v, u, nxt);
        }
    };
    const baseCnt = dfs1(0, -1);
    dfs2(0, -1, baseCnt);
    return ans;
}
