// LeetCode 0654 - Maximum Binary Tree
// https://leetcode.com/problems/maximum-binary-tree/

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

export function constructMaximumBinaryTree(nums: number[]): TreeNode | null {
    const build = (left, right) => {
        if (left > right) return null;
        let mid = left;
        for (let i = left; i <= right; ++i) if (nums[i] > nums[mid]) mid = i;
        return new TreeNode(nums[mid], build(left, mid - 1), build(mid + 1, right));
    };
    return build(0, nums.length - 1);
}
