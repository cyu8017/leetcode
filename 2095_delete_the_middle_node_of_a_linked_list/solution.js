// LeetCode 2095 - Delete the Middle Node of a Linked List
// https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteMiddle = function(head) {
    if (head.next === null) return null;
    let slow = head, fast = head, prev = null;
    while (fast !== null && fast.next !== null) {
        prev = slow;
        slow = slow.next;
        fast = fast.next.next;
    }
    prev.next = slow.next;
    return head;
};
