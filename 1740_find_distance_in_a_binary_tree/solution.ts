// LeetCode 1740 - Find Distance in a Binary Tree
// https://leetcode.com/problems/find-distance-in-a-binary-tree/

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val ?? 0;
        this.left = left ?? null;
        this.right = right ?? null;
    }
}

function findDistance(root: TreeNode | null, p: number, q: number): number {
    const graph = new Map<number, number[]>();
    const dfs = (node: TreeNode | null, parent: TreeNode | null): void => {
        if (!node) {
            return;
        }
        if (!graph.has(node.val)) {
            graph.set(node.val, []);
        }
        if (parent) {
            graph.get(node.val)!.push(parent.val);
            graph.get(parent.val)!.push(node.val);
        }
        dfs(node.left, node);
        dfs(node.right, node);
    };
    dfs(root, null);
    const queue: [number, number][] = [[p, 0]];
    const seen = new Set<number>([p]);
    while (queue.length > 0) {
        const [node, dist] = queue.shift()!;
        if (node === q) {
            return dist;
        }
        for (const nei of graph.get(node)!) {
            if (!seen.has(nei)) {
                seen.add(nei);
                queue.push([nei, dist + 1]);
            }
        }
    }
    return -1;
}
