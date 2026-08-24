// LeetCode 2130 - Maximum Twin Sum of a Linked List
// https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {number}
 */
var pairSum = function(head) {
    let slow = head, fast = head;
    while (fast !== null && fast.next !== null) {
        slow = slow.next;
        fast = fast.next.next;
    }
    let prev = null;
    while (slow !== null) {
        const nxt = slow.next;
        slow.next = prev;
        prev = slow;
        slow = nxt;
    }
    let ans = 0;
    let a = head, b = prev;
    while (b !== null) {
        ans = Math.max(ans, a.val + b.val);
        a = a.next;
        b = b.next;
    }
    return ans;
};
