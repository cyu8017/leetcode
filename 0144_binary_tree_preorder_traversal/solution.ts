// LeetCode 0144 - Binary Tree Preorder Traversal
// https://leetcode.com/problems/binary-tree-preorder-traversal/

interface TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
}

export function preorderTraversal(root: TreeNode | null): number[] {
  const result: number[] = [];

  const traverse = (node: TreeNode | null): void => {
    if (!node) return;
    result.push(node.val);
    traverse(node.left);
    traverse(node.right);
  };

  traverse(root);
  return result;
}