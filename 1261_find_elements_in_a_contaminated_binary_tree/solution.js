// LeetCode 1261 - Find Elements in a Contaminated Binary Tree
// https://leetcode.com/problems/find-elements-in-a-contaminated-binary-tree/

function listToTree(values) {
    if (!values || values.length === 0) return null;
    const root = { val: values[0], left: null, right: null };
    const queue = [root];
    let i = 1;
    while (queue.length > 0 && i < values.length) {
        const node = queue.shift();
        if (i < values.length && values[i] !== null && values[i] !== undefined) {
            node.left = { val: values[i], left: null, right: null };
            queue.push(node.left);
        }
        i += 1;
        if (i < values.length && values[i] !== null && values[i] !== undefined) {
            node.right = { val: values[i], left: null, right: null };
            queue.push(node.right);
        }
        i += 1;
    }
    return root;
}

/**
 * @param {TreeNode} root
 */
var FindElements = function(root) {
    this.values = new Set();
    if (Array.isArray(root)) {
        root = listToTree(root);
    }
    const recover = (node, value) => {
        if (!node) return;
        node.val = value;
        this.values.add(value);
        recover(node.left, 2 * value + 1);
        recover(node.right, 2 * value + 2);
    };
    recover(root, 0);
};

/**
 * @param {number} target
 * @return {boolean}
 */
FindElements.prototype.find = function(target) {
    return this.values.has(target);
};
