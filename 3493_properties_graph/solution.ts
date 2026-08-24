// LeetCode 3493 - Properties Graph
// https://leetcode.com/problems/properties-graph/

export function numberOfComponents(properties: any, k: any): any {
    const n = properties.length;
    const sets = properties.map((row) => new Set(row));
    const parent = Array.from({ length: n }, (_, i) => i);
    const find = (x) => {
        if (parent[x] !== x) parent[x] = find(parent[x]);
        return parent[x];
    };
    const unite = (a, b) => {
        const ra = find(a), rb = find(b);
        if (ra !== rb) parent[ra] = rb;
    };
    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            let cnt = 0;
            for (const v of sets[i]) if (sets[j].has(v)) cnt++;
            if (cnt >= k) unite(i, j);
        }
    }
    const comp = new Set();
    for (let i = 0; i < n; i++) comp.add(find(i));
    return comp.size;
}
