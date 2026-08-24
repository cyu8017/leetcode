// LeetCode 2181 - Merge Nodes in Between Zeros
// https://leetcode.com/problems/merge-nodes-in-between-zeros/

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
var mergeNodes = function(head) {
    const dummy = new ListNode();
    let cur = dummy;
    let sum = 0;
    for (let p = head.next; p !== null; p = p.next) {
        if (p.val === 0) {
            cur.next = new ListNode(sum);
            cur = cur.next;
            sum = 0;
        } else sum += p.val;
    }
    return dummy.next;
};
