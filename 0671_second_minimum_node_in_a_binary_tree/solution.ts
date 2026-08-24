// LeetCode 0671 - Second Minimum Node In a Binary Tree
// https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/

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

class Node {
    val: number;
    children: Node[];
    constructor(val?: number, children?: Node[]) {
        this.val = val ?? 0;
        this.children = children ?? [];
    }
}

export function findSecondMinimumValue(root: TreeNode | null): number {
    if (root == null) return -1;
    let ans = -1;
    const rootVal = root.val;
    const dfs = (node) => {
        if (node == null) return;
        if (node.val > rootVal) {
            if (ans === -1 || node.val < ans) ans = node.val;
            return;
        }
        dfs(node.left);
        dfs(node.right);
    };
    dfs(root);
    return ans;
}
