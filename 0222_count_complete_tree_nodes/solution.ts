// LeetCode 0222 - Count Complete Tree Nodes
// https://leetcode.com/problems/count-complete-tree-nodes/

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

function leftDepth(node: TreeNode | null): number {
    let depth = 0;
    while (node) {
        depth += 1;
        node = node.left;
    }
    return depth;
}

function rightDepth(node: TreeNode | null): number {
    let depth = 0;
    while (node) {
        depth += 1;
        node = node.right;
    }
    return depth;
}

export function countNodes(root: TreeNode | null): number {
    if (!root) {
        return 0;
    }
    const left = leftDepth(root);
    const right = rightDepth(root);
    if (left === right) {
        return (1 << left) - 1;
    }
    return 1 + countNodes(root.left) + countNodes(root.right);
}
