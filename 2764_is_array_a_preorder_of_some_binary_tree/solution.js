// LeetCode 2764 - Is Array a Preorder of Some Binary Tree
// https://leetcode.com/problems/is-array-a-preorder-of-some-binary-tree/

/**
 * @param {number[][]} nodes
 * @return {boolean}
 */
var isPreorder = function(nodes) {
    if (!nodes.length) return true;
    const stack = [nodes[0][0]];
    for (let i = 1; i < nodes.length; i++) {
        const id = nodes[i][0], parent = nodes[i][1];
        while (stack.length && stack[stack.length - 1] !== parent) stack.pop();
        if (!stack.length) return false;
        stack.push(id);
    }
    return true;
};
