// LeetCode 0662 - Maximum Width of Binary Tree
// https://leetcode.com/problems/maximum-width-of-binary-tree/

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

export function widthOfBinaryTree(root: TreeNode | null): number {
    if (root == null) return 0;
    const queue = [[root, 0n]];
    let best = 0;
    while (queue.length) {
        const left = queue[0][1];
        const size = queue.length;
        for (let i = 0; i < size; ++i) {
            const [node, idx] = queue.shift();
            best = Math.max(best, Number(idx - left + 1n));
            if (node.left) queue.push([node.left, idx * 2n]);
            if (node.right) queue.push([node.right, idx * 2n + 1n]);
        }
    }
    return best;
}
