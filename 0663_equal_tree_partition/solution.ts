// LeetCode 0663 - Equal Tree Partition
// https://leetcode.com/problems/equal-tree-partition/

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

export function checkEqualTree(root: TreeNode | null): boolean {
    const subtreeSums = [];
    const dfs = (node) => {
        if (node == null) return 0;
        const total = node.val + dfs(node.left) + dfs(node.right);
        subtreeSums.push(total);
        return total;
    };
    const total = dfs(root);
    if (subtreeSums.length) subtreeSums.pop();
    if (total % 2 !== 0) return false;
    const half = total / 2;
    return subtreeSums.includes(half);
}
