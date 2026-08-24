// LeetCode 0563 - Binary Tree Tilt
// https://leetcode.com/problems/binary-tree-tilt/

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

export function findTilt(root: TreeNode | null): number {
    let total = 0;
    const subtreeSum = (node) => {
        if (node == null) return 0;
        const left = subtreeSum(node.left);
        const right = subtreeSum(node.right);
        total += Math.abs(left - right);
        return node.val + left + right;
    };
    subtreeSum(root);
    return total;
}
