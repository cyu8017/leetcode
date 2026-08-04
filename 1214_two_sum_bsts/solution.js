// LeetCode 1214 - Two Sum BSTs
// https://leetcode.com/problems/two-sum-bsts/

/**
 * @param {TreeNode} root1
 * @param {TreeNode} root2
 * @param {number} target
 * @return {boolean}
 */
var twoSumBSTs = function(root1, root2, target) {
    const values = new Set();
    const stack = root1 ? [root1] : [];
    while (stack.length) {
        const node = stack.pop();
        values.add(node.val);
        if (node.left) stack.push(node.left);
        if (node.right) stack.push(node.right);
    }
    const stack2 = root2 ? [root2] : [];
    while (stack2.length) {
        const node = stack2.pop();
        if (values.has(target - node.val)) return true;
        if (node.left) stack2.push(node.left);
        if (node.right) stack2.push(node.right);
    }
    return false;
};
