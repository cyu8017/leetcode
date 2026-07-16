// LeetCode 0129 - Sum Root to Leaf Numbers
// https://leetcode.com/problems/sum-root-to-leaf-numbers/

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

export function sumNumbers(root: TreeNode | null): number {
    const dfs = (node: TreeNode | null, current: number): number => {
        if (!node) {
            return 0;
        }

        const value = current * 10 + node.val;
        if (!node.left && !node.right) {
            return value;
        }
        return dfs(node.left, value) + dfs(node.right, value);
    };

    return dfs(root, 0);
}