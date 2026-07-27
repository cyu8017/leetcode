// LeetCode 1697 - Checking Existence of Edge Length Limited Paths
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths/

function distanceLimitedPathsExist(n: number, edgeList: number[][], queries: number[][]): boolean[] {
    const parent = Array.from({ length: n }, (_, i) => i);
    const find = (x: number): number => {
        while (x !== parent[x]) {
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;
    };
    const ans = Array(queries.length).fill(false);
    const edges = [...edgeList].sort((a, b) => a[2] - b[2]);
    const qs = queries.map((q, j) => [q[2], q[0], q[1], j]).sort((a, b) => a[0] - b[0]);
    let i = 0;
    for (const [limit, p, q, idx] of qs) {
        while (i < edges.length && edges[i][2] < limit) {
            const [a, b] = edges[i];
            parent[find(a)] = find(b);
            i++;
        }
        ans[idx] = find(p) === find(q);
    }
    return ans;
}
