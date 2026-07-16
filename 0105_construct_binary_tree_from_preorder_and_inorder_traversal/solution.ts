// LeetCode 0105 - Construct Binary Tree from Preorder and Inorder Traversal
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

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

export function buildTree(preorder: number[], inorder: number[]): TreeNode | null {
    const index = new Map<number, number>();
    for (let i = 0; i < inorder.length; i++) {
        index.set(inorder[i], i);
    }
    let preIndex = 0;

    function build(left: number, right: number): TreeNode | null {
        if (left > right) {
            return null;
        }
        const rootVal = preorder[preIndex++];
        const mid = index.get(rootVal)!;
        const root = new TreeNode(rootVal);
        root.left = build(left, mid - 1);
        root.right = build(mid + 1, right);
        return root;
    }

    return build(0, inorder.length - 1);
}