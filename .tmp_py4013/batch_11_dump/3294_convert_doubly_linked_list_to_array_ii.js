// LeetCode 3294 - Convert Doubly Linked List to Array II
// https://leetcode.com/problems/convert-doubly-linked-list-to-array-ii/

/**
 * // Definition for a Node.
 * function Node(val, prev, next) {
 *    this.val = val;
 *    this.prev = prev;
 *    this.next = next;
 * };
 */
var toArray = function(node) {
    while (node !== null && node.prev !== null) node = node.prev;
    const ans = [];
    while (node !== null) {
        ans.push(node.val);
        node = node.next;
    }
    return ans;
};
