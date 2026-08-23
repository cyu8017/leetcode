// LeetCode 0144 - Binary Tree Preorder Traversal
// https://leetcode.com/problems/binary-tree-preorder-traversal/

/**
 * @param {{ val: number, left: object|null, right: object|null }|null} root
 * @return {number[]}
 */
var preorderTraversal = function(root) {
  const result = [];

  const traverse = (node) => {
    if (!node) return;
    result.push(node.val);
    traverse(node.left);
    traverse(node.right);
  };

  traverse(root);
  return result;
};