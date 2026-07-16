// LeetCode 0113 - Path Sum II
// https://leetcode.com/problems/path-sum-ii/

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

export function pathSum(root: TreeNode | null, targetSum: number): number[][] {
    const result: number[][] = [];

    function visit(node: TreeNode | null, remaining: number, path: number[]): void {
        if (!node) {
            return;
        }
        path.push(node.val);
        if (!node.left && !node.right && remaining === node.val) {
            result.push([...path]);
        } else {
            visit(node.left, remaining - node.val, path);
            visit(node.right, remaining - node.val, path);
        }
        path.pop();
    }

    visit(root, targetSum, []);
    return result;
}