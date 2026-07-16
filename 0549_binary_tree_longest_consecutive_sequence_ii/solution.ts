// LeetCode 0549 - Binary Tree Longest Consecutive Sequence II
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/

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
    longestConsecutive(root: TreeNode | null): number {
        let best = 0;

        const dfs = (node: TreeNode | null): [number, number] => {
            if (!node) return [0, 0];

            const [leftInc, leftDec] = dfs(node.left);
            const [rightInc, rightDec] = dfs(node.right);

            let inc = 1;
            let dec = 1;
            if (node.left) {
                if (node.left.val === node.val + 1) inc = Math.max(inc, leftInc + 1);
                else if (node.left.val === node.val - 1) dec = Math.max(dec, leftDec + 1);
            }
            if (node.right) {
                if (node.right.val === node.val + 1) inc = Math.max(inc, rightInc + 1);
                else if (node.right.val === node.val - 1) dec = Math.max(dec, rightDec + 1);
            }

            if (node.left && node.right) {
                if (node.left.val + 1 === node.val && node.val === node.right.val - 1) {
                    best = Math.max(best, leftDec + 1 + rightInc);
                }
                if (node.left.val - 1 === node.val && node.val === node.right.val + 1) {
                    best = Math.max(best, leftInc + 1 + rightDec);
                }
            }

            best = Math.max(best, inc, dec);
            return [inc, dec];
        };

        dfs(root);
        return best;
    }
}
