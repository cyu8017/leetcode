// LeetCode 0261 - Graph Valid Tree
// https://leetcode.com/problems/graph-valid-tree/

export function validTree(n: number, edges: number[][]): boolean {
    if (edges.length !== n - 1) {
        return false;
    }
    const parent = Array.from({ length: n }, (_, i) => i);

    function find(node: number): number {
        if (parent[node] !== node) {
            parent[node] = find(parent[node]);
        }
        return parent[node];
    }

    for (const [left, right] of edges) {
        const rootLeft = find(left);
        const rootRight = find(right);
        if (rootLeft === rootRight) {
            return false;
        }
        parent[rootLeft] = rootRight;
    }
    return true;
}
