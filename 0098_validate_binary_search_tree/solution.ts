// LeetCode 0098 - Validate Binary Search Tree
// https://leetcode.com/problems/validate-binary-search-tree/

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

export function isValidBST(root: TreeNode | null): boolean {
    function valid(node: TreeNode | null, low: number, high: number): boolean {
        if (!node) {
            return true;
        }
        if (!(low < node.val && node.val < high)) {
            return false;
        }
        return valid(node.left, low, node.val) && valid(node.right, node.val, high);
    }

    return valid(root, -Infinity, Infinity);
}
