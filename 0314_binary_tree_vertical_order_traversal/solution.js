// LeetCode 0314 - Binary Tree Vertical Order Traversal
// https://leetcode.com/problems/binary-tree-vertical-order-traversal/

/**
 * @param {TreeNode|null} root
 * @return {number[][]}
 */
var verticalOrder = function(root) {
    if (!root) {
        return [];
    }
    const columns = new Map();
    const queue = [[root, 0]];
    let minCol = 0;
    let maxCol = 0;
    while (queue.length > 0) {
        const [node, column] = queue.shift();
        minCol = Math.min(minCol, column);
        maxCol = Math.max(maxCol, column);
        if (!columns.has(column)) {
            columns.set(column, []);
        }
        columns.get(column).push(node.val);
        if (node.left) {
            queue.push([node.left, column - 1]);
        }
        if (node.right) {
            queue.push([node.right, column + 1]);
        }
    }
    const result = [];
    for (let column = minCol; column <= maxCol; column += 1) {
        result.push(columns.get(column) || []);
    }
    return result;
};
