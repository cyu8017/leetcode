// LeetCode 2415 - Reverse Odd Levels of Binary Tree
// https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/

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

export function reverseOddLevels(root: TreeNode | null): TreeNode | null {
    const dfs = (a, b, level) => {
        if (a === null || b === null) return;
        if (level % 2 === 1) {
            const tmp = a.val;
            a.val = b.val;
            b.val = tmp;
        }
        dfs(a.left, b.right, level + 1);
        dfs(a.right, b.left, level + 1);
    };
    if (root !== null) dfs(root.left, root.right, 1);
    return root;
}
