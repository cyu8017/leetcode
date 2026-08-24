// LeetCode 0652 - Find Duplicate Subtrees
// https://leetcode.com/problems/find-duplicate-subtrees/

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

export function findDuplicateSubtrees(root: TreeNode | null): TreeNode | null[] {
    const counts = new Map();
    const result = [];
    const serialize = (node) => {
        if (node == null) return "#";
        const key = node.val + "," + serialize(node.left) + "," + serialize(node.right);
        const count = (counts.get(key) || 0) + 1;
        counts.set(key, count);
        if (count === 2) result.push(node);
        return key;
    };
    serialize(root);
    return result;
}
