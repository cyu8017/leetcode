// LeetCode 0250 - Count Univalue Subtrees
// https://leetcode.com/problems/count-univalue-subtrees/

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

export function countUnivalSubtrees(root: TreeNode | null): number {
    let count = 0;

    const dfs = (node: TreeNode | null): boolean => {
        if (!node) {
            return true;
        }
        const leftOk = dfs(node.left);
        const rightOk = dfs(node.right);
        if (!leftOk || !rightOk) {
            return false;
        }
        if (node.left && node.left.val !== node.val) {
            return false;
        }
        if (node.right && node.right.val !== node.val) {
            return false;
        }
        count += 1;
        return true;
    };

    dfs(root);
    return count;
}
