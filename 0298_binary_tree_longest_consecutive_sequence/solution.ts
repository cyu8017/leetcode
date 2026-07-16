// LeetCode 0298 - Binary Tree Longest Consecutive Sequence
// https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

export class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = val ?? 0;
        this.left = left ?? null;
        this.right = right ?? null;
    }
}

export function longestConsecutive(root: TreeNode | null): number {
    function dfs(node: TreeNode | null, parent: TreeNode | null, length: number): number {
        if (!node) {
            return 0;
        }
        const current = parent && parent.val + 1 === node.val ? length + 1 : 1;
        return Math.max(current, dfs(node.left, node, current), dfs(node.right, node, current));
    }
    return dfs(root, null, 0);
}
