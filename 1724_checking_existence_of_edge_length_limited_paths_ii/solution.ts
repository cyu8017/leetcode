// LeetCode 1724 - Checking Existence of Edge Length Limited Paths II
// https://leetcode.com/problems/checking-existence-of-edge-length-limited-paths-ii/

export class DistanceLimitedPathsExist {
    private readonly weights: number[] = [];
    private readonly versions: number[][] = [];

    constructor(n: number, edgeList: number[][]) {
        const edges = edgeList
            .map(([u, v, w]) => [w, u, v])
            .sort((a, b) => a[0] - b[0] || a[1] - b[1] || a[2] - b[2]);
        const parent = Array.from({ length: n }, (_, i) => i);
        const size = new Array<number>(n).fill(1);
        const find = (x: number): number => {
            while (parent[x] !== x) {
                parent[x] = parent[parent[x]];
                x = parent[x];
            }
            return x;
        };
        const union = (a: number, b: number): void => {
            let ra = find(a);
            let rb = find(b);
            if (ra === rb) return;
            if (size[ra] < size[rb]) [ra, rb] = [rb, ra];
            parent[rb] = ra;
            size[ra] += size[rb];
        };
        let i = 0;
        while (i < edges.length) {
            const weight = edges[i][0];
            while (i < edges.length && edges[i][0] === weight) {
                union(edges[i][1], edges[i][2]);
                i++;
            }
            this.weights.push(weight);
            this.versions.push([...parent]);
        }
    }

    query(p: number, q: number, limit: number): boolean {
        let lo = 0;
        let hi = this.weights.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (this.weights[mid] < limit) lo = mid + 1;
            else hi = mid;
        }
        const idx = lo - 1;
        if (idx < 0) return p === q;
        const parent = this.versions[idx];
        const find = (x: number): number => {
            while (parent[x] !== x) x = parent[x];
            return x;
        };
        return find(p) === find(q);
    }
}
