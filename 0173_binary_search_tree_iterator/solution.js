// LeetCode 0173 - Binary Search Tree Iterator
// https://leetcode.com/problems/binary-search-tree-iterator/

class BSTIterator {
    /**
     * @param {{ val: number, left: object|null, right: object|null }|null} root
     */
    constructor(root) {
        this.stack = [];
        this.pushLeft(root);
    }

    /**
     * @param {object|null} node
     * @return {void}
     */
    pushLeft(node) {
        while (node) {
            this.stack.push(node);
            node = node.left;
        }
    }

    /**
     * @return {number}
     */
    next() {
        const node = this.stack.pop();
        this.pushLeft(node.right);
        return node.val;
    }

    /**
     * @return {boolean}
     */
    hasNext() {
        return this.stack.length > 0;
    }
}

module.exports = { BSTIterator };