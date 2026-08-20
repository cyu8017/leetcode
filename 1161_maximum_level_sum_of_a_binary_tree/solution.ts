// LeetCode 1161 - Maximum Level Sum of a Binary Tree
// https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/

class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
    constructor(val = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

function maxLevelSum(root: TreeNode | null): number {
    const queue = [root];
    let bestSum = -Infinity, bestLevel = 1, level = 1;
    while (queue.length) {
        const size = queue.length;
        let total = 0;
        for (let i = 0; i < size; i++) {
            const node = queue.shift();
            total += node.val;
            if (node.left) queue.push(node.left);
            if (node.right) queue.push(node.right);
        }
        if (total > bestSum) {
            bestSum = total;
            bestLevel = level;
        }
        level++;
    }
    return bestLevel;
}
