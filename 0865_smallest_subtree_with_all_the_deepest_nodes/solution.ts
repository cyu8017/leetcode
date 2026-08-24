// LeetCode 0865 - Smallest Subtree with all the Deepest Nodes
// https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

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

export function subtreeWithAllDeepest(root: TreeNode | null): TreeNode | null {
    const dfs = (node) => {
        if (!node) return { depth: 0, node: null };
        const left = dfs(node.left);
        const right = dfs(node.right);
        if (left.depth > right.depth) return { depth: left.depth + 1, node: left.node };
        if (right.depth > left.depth) return { depth: right.depth + 1, node: right.node };
        return { depth: left.depth + 1, node: node };
    };
    return dfs(root).node;
}
