"use strict";
// LeetCode 1586 - Binary Search Tree Iterator II
// https://leetcode.com/problems/binary-search-tree-iterator-ii/
// @ts-nocheck
Object.defineProperty(exports, "__esModule", { value: true });
exports.BSTIterator = void 0;
class BSTIterator {
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
    hasNext() {
        return this.index + 1 < this.values.length;
    }
    next() {
        this.index++;
        return this.values[this.index];
    }
    hasPrev() {
        return this.index > 0;
    }
    prev() {
        this.index--;
        return this.values[this.index];
    }
}
exports.BSTIterator = BSTIterator;
