// LeetCode 0145 - Binary Tree Postorder Traversal
// https://leetcode.com/problems/binary-tree-postorder-traversal/

interface TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
}

export function postorderTraversal(root: TreeNode | null): number[] {
  const result: number[] = [];

  const traverse = (node: TreeNode | null): void => {
    if (!node) return;
    traverse(node.left);
    traverse(node.right);
    result.push(node.val);
  };

  traverse(root);
  return result;
}