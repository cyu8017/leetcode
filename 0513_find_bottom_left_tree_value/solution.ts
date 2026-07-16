// LeetCode 0513 - Find Bottom Left Tree Value
// https://leetcode.com/problems/find-bottom-left-tree-value/

export class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(val = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

export class Solution {
    findBottomLeftValue(root: TreeNode): number {
        const queue: TreeNode[] = [root];
        let leftmost = root.val;
        while (queue.length) {
            const levelSize = queue.length;
            for (let index = 0; index < levelSize; index += 1) {
                const node = queue.shift() as TreeNode;
                if (index === 0) leftmost = node.val;
                if (node.left) queue.push(node.left);
                if (node.right) queue.push(node.right);
            }
        }
        return leftmost;
    }
}
