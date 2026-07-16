// LeetCode 0257 - Binary Tree Paths
// https://leetcode.com/problems/binary-tree-paths/

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

export function binaryTreePaths(root: TreeNode | null): string[] {
    const result: string[] = [];

    const dfs = (node: TreeNode | null, path: string[]): void => {
        if (!node) {
            return;
        }
        path.push(String(node.val));
        if (!node.left && !node.right) {
            result.push(path.join('->'));
        } else {
            dfs(node.left, path);
            dfs(node.right, path);
        }
        path.pop();
    };

    dfs(root, []);
    return result;
}
