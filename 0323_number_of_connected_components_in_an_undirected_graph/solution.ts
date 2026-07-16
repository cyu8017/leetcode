export function countComponents(n: number, edges: number[][]): number {
    const parent = Array.from({ length: n }, (_, index) => index);
    const rank = Array(n).fill(0);
    function find(node: number): number {
        if (parent[node] !== node) parent[node] = find(parent[node]);
        return parent[node];
    }
    let components = n;
    for (const [left, right] of edges) {
        const rootLeft = find(left);
        const rootRight = find(right);
        if (rootLeft === rootRight) continue;
        if (rank[rootLeft] < rank[rootRight]) parent[rootLeft] = rootRight;
        else {
            parent[rootRight] = rootLeft;
            if (rank[rootLeft] === rank[rootRight]) rank[rootLeft] += 1;
        }
        components -= 1;
    }
    return components;
}
