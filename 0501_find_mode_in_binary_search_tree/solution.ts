// LeetCode 0501 - Find Mode in Binary Search Tree
// https://leetcode.com/problems/find-mode-in-binary-search-tree/

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
    findMode(root: TreeNode | null): number[] {
        const counts = new Map<number, number>();
        let best = 0;
        const inorder = (node: TreeNode | null): void => {
            if (!node) return;
            inorder(node.left);
            counts.set(node.val, (counts.get(node.val) || 0) + 1);
            best = Math.max(best, counts.get(node.val) as number);
            inorder(node.right);
        };
        inorder(root);
        return [...counts.entries()].filter(([, count]) => count === best).map(([value]) => value);
    }
}
