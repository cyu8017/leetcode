// LeetCode 0116 - Populating Next Right Pointers in Each Node
// https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

function Node(val, left, right, next) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
    this.next = (next === undefined ? null : next);
}

/**
 * @param {Node} root
 * @return {Node}
 */
var connect = function(root) {
    if (!root) {
        return root;
    }

    let level = [root];
    while (level.length) {
        for (let index = 0; index < level.length; index++) {
            level[index].next = index + 1 < level.length ? level[index + 1] : null;
        }
        const nextLevel = [];
        for (const node of level) {
            if (node.left) nextLevel.push(node.left);
            if (node.right) nextLevel.push(node.right);
        }
        level = nextLevel;
    }
    return root;
};