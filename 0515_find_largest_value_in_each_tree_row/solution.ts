// LeetCode 0515 - Find Largest Value in Each Tree Row
// https://leetcode.com/problems/find-largest-value-in-each-tree-row/

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
    largestValues(root: TreeNode | null): number[] {
        if (!root) return [];
        const result: number[] = [];
        const queue: TreeNode[] = [root];
        while (queue.length) {
            let levelMax = -Infinity;
            for (let count = queue.length; count > 0; count -= 1) {
                const node = queue.shift() as TreeNode;
                levelMax = Math.max(levelMax, node.val);
                if (node.left) queue.push(node.left);
                if (node.right) queue.push(node.right);
            }
            result.push(levelMax);
        }
        return result;
    }
}
