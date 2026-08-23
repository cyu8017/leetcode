// LeetCode 0206 - Reverse Linked List
// https://leetcode.com/problems/reverse-linked-list/

/**
 * @param {number} val
 * @param {ListNode|null} next
 */
function ListNode(val = 0, next = null) {
    this.val = val;
    this.next = next;
}

/**
 * @param {ListNode|null} head
 * @return {ListNode|null}
 */
var reverseList = function(head) {
    let previous = null;
    let current = head;
    while (current) {
        const next = current.next;
        current.next = previous;
        previous = current;
        current = next;
    }
    return previous;
};