// LeetCode 0637 - Average of Levels in Binary Tree
// https://leetcode.com/problems/average-of-levels-in-binary-tree/

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

export function averageOfLevels(root: TreeNode | null): number[] {
    const result = [];
    if (root == null) return result;
    const queue = [root];
    while (queue.length) {
        const count = queue.length;
        let total = 0;
        for (let i = 0; i < count; ++i) {
            const node = queue.shift();
            total += node.val;
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        result.push(total / count);
    }
    return result;
}
