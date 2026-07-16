// LeetCode 0108 - Convert Sorted Array to Binary Search Tree
// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

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

export function sortedArrayToBST(nums: number[]): TreeNode | null {
    function build(left: number, right: number): TreeNode | null {
        if (left > right) {
            return null;
        }
        const mid = Math.floor((left + right + 1) / 2);
        const root = new TreeNode(nums[mid]);
        root.left = build(left, mid - 1);
        root.right = build(mid + 1, right);
        return root;
    }
    return build(0, nums.length - 1);
}
