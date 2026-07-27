// LeetCode 1617 - Count Subtrees With Max Distance Between Cities
// https://leetcode.com/problems/count-subtrees-with-max-distance-between-cities/

function countSubgraphsForEachDiameter(n: number, edges: number[][]): number[] {
    const adj: number[][] = Array.from({ length: n }, () => []);
    for (let [a, b] of edges) {
        a--; b--;
        adj[a].push(b);
        adj[b].push(a);
    }
    const ans = Array(n - 1).fill(0);
    const bitCount = (mask: number): number => {
        let c = 0;
        while (mask) {
            c += mask & 1;
            mask >>= 1;
        }
        return c;
    };
    for (let mask = 1; mask < (1 << n); mask++) {
        if ((mask & (mask - 1)) === 0) continue;
        let start = 0;
        while (!((mask >> start) & 1)) start++;
        const bfs = (src: number): [number, Map<number, number>] => {
            const dist = new Map<number, number>([[src, 0]]);
            const q = [src];
            for (const u of q) {
                for (const v of adj[u]) {
                    if (((mask >> v) & 1) && !dist.has(v)) {
                        dist.set(v, dist.get(u)! + 1);
                        q.push(v);
                    }
                }
            }
            let far = src;
            for (const [node, d] of dist) if (d > dist.get(far)!) far = node;
            return [far, dist];
        };
        const [far, seen] = bfs(start);
        if (seen.size === bitCount(mask)) {
            const [, dist] = bfs(far);
            let mx = 0;
            for (const d of dist.values()) mx = Math.max(mx, d);
            ans[mx - 1]++;
        }
    }
    return ans;
}
