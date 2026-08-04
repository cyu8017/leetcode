// LeetCode 1586 - Binary Search Tree Iterator II
// https://leetcode.com/problems/binary-search-tree-iterator-ii/

class BSTIterator {
    /**
     * @param {TreeNode} root
     */
    constructor(root) {
        this.values = [];
        const stack = [];
        while (stack.length || root) {
            while (root) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();
            this.values.push(root.val);
            root = root.right;
        }
        this.index = -1;
    }

    /**
     * @return {boolean}
     */
    hasNext() {
        return this.index + 1 < this.values.length;
    }

    /**
     * @return {number}
     */
    next() {
        this.index++;
        return this.values[this.index];
    }

    /**
     * @return {boolean}
     */
    hasPrev() {
        return this.index > 0;
    }

    /**
     * @return {number}
     */
    prev() {
        this.index--;
        return this.values[this.index];
    }
}

module.exports = { BSTIterator };
