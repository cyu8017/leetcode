// LeetCode 0095 - Unique Binary Search Trees II
// https://leetcode.com/problems/unique-binary-search-trees-ii/

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

export function generateTrees(n: number): Array<TreeNode | null> {
    function build(start: number, end: number): Array<TreeNode | null> {
        if (start > end) {
            return [null];
        }
        const trees: Array<TreeNode | null> = [];
        for (let rootVal = start; rootVal <= end; rootVal++) {
            const leftTrees = build(start, rootVal - 1);
            const rightTrees = build(rootVal + 1, end);
            for (const left of leftTrees) {
                for (const right of rightTrees) {
                    trees.push(new TreeNode(rootVal, left, right));
                }
            }
        }
        return trees;
    }
    return n ? build(1, n) : [];
}
