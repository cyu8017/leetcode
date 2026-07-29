// LeetCode 1038 - Binary Search Tree to Greater Sum Tree
// https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
function bstToGst(root) {
    let total = 0;
    const reverseInorder = (node) => {
        if (!node)
            return;
        reverseInorder(node.right);
        total += node.val;
        node.val = total;
        reverseInorder(node.left);
    };
    reverseInorder(root);
    return root;
}
