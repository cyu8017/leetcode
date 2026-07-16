// LeetCode 0199 - Binary Tree Right Side View
// https://leetcode.com/problems/binary-tree-right-side-view/

function TreeNode(val = 0, left = null, right = null) {
    this.val = val;
    this.left = left;
    this.right = right;
}

/**
 * @param {TreeNode|null} root
 * @return {number[]}
 */
var rightSideView = function(root) {
    if (!root) {
        return [];
    }

    const result = [];
    const queue = [root];
    let head = 0;
    while (head < queue.length) {
        const levelEnd = queue.length;
        while (head < levelEnd) {
            const node = queue[head++];
            if (head === levelEnd) {
                result.push(node.val);
            }
            if (node.left) {
                queue.push(node.left);
            }
            if (node.right) {
                queue.push(node.right);
            }
        }
    }
    return result;
};