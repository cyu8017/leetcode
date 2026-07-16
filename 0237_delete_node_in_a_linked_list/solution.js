// LeetCode 0237 - Delete Node in a Linked List
// https://leetcode.com/problems/delete-node-in-a-linked-list/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val);
    this.next = (next === undefined ? null : next);
}

/**
 * @param {ListNode} node
 * @return {void}
 */
var deleteNode = function(node) {
    node.val = node.next.val;
    node.next = node.next.next;
};
