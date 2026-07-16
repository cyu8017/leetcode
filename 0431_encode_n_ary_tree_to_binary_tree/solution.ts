// LeetCode 0431 - Encode N-ary Tree to Binary Tree
// https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/

export class Node {
    val: number | null;
    children: Node[];

    constructor(val: number | null = null, children: Node[] | null = null) {
        this.val = val;
        this.children = children ?? [];
    }
}

export class TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;

    constructor(val = 0, left: TreeNode | null = null, right: TreeNode | null = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

export class Solution {
    encodeNaryTree(root: Node | null): TreeNode | null {
        if (!root) return null;
        const binary = new TreeNode(root.val as number);
        if (!root.children.length) return binary;
        binary.left = this.encodeNaryTree(root.children[0]);
        let sibling = binary.left;
        for (let i = 1; i < root.children.length; i += 1) {
            sibling!.right = this.encodeNaryTree(root.children[i]);
            sibling = sibling!.right;
        }
        return binary;
    }

    decodeBinaryTree(root: TreeNode | null): Node | null {
        if (!root) return null;
        const node = new Node(root.val, []);
        let current = root.left;
        while (current) {
            node.children.push(this.decodeBinaryTree(current) as Node);
            current = current.right;
        }
        return node;
    }
}
