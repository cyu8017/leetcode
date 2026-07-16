// LeetCode 0107 - Binary Tree Level Order Traversal II
// https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

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

export function levelOrderBottom(root: TreeNode | null): number[][] {
    if (!root) {
        return [];
    }

    const result: number[][] = [];
    const queue: TreeNode[] = [root];

    while (queue.length > 0) {
        const level: number[] = [];
        const size = queue.length;
        for (let i = 0; i < size; i++) {
            const node = queue.shift()!;
            level.push(node.val);
            if (node.left) {
                queue.push(node.left);
            }
            if (node.right) {
                queue.push(node.right);
            }
        }
        result.push(level);
    }

    result.reverse();
    return result;
}
