// LeetCode 0145 - Binary Tree Postorder Traversal
// https://leetcode.com/problems/binary-tree-postorder-traversal/

/**
 * @param {{ val: number, left: object|null, right: object|null }|null} root
 * @return {number[]}
 */
var postorderTraversal = function(root) {
  const result = [];

  const traverse = (node) => {
    if (!node) return;
    traverse(node.left);
    traverse(node.right);
    result.push(node.val);
  };

  traverse(root);
  return result;
};