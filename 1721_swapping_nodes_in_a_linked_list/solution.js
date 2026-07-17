// LeetCode 1721 - Swapping Nodes in a Linked List
// https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var swapNodes = function(head, k) {
    let first = head;
    for (let i = 0; i < k - 1; i++) {
        first = first.next;
    }
    let fast = first;
    let second = head;
    while (fast.next) {
        fast = fast.next;
        second = second.next;
    }
    const temp = first.val;
    first.val = second.val;
    second.val = temp;
    return head;
};
