// LeetCode 1038 - Binary Search Tree to Greater Sum Tree
// https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

interface TreeNode {
    val: number;
    left: TreeNode | null;
    right: TreeNode | null;
}

function bstToGst(root: TreeNode | null): TreeNode | null {
    let total = 0;
    const reverseInorder = (node: TreeNode | null): void => {
        if (!node) return;
        reverseInorder(node.right);
        total += node.val;
        node.val = total;
        reverseInorder(node.left);
    };
    reverseInorder(root);
    return root;
}
