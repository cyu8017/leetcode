// LeetCode 0106 - Construct Binary Tree from Inorder and Postorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

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

export function buildTree(inorder: number[], postorder: number[]): TreeNode | null {
    const index = new Map<number, number>();
    for (let i = 0; i < inorder.length; i++) {
        index.set(inorder[i], i);
    }
    let postIndex = postorder.length - 1;

    function build(left: number, right: number): TreeNode | null {
        if (left > right) {
            return null;
        }
        const rootVal = postorder[postIndex--];
        const mid = index.get(rootVal)!;
        const root = new TreeNode(rootVal);
        root.right = build(mid + 1, right);
        root.left = build(left, mid - 1);
        return root;
    }

    return build(0, inorder.length - 1);
}