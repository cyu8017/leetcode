// LeetCode 0203 - Remove Linked List Elements
// https://leetcode.com/problems/remove-linked-list-elements/

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
 * @param {number} val
 * @return {ListNode|null}
 */
var removeElements = function(head, val) {
    const dummy = new ListNode(0, head);
    let current = dummy;
    while (current.next) {
        if (current.next.val === val) {
            current.next = current.next.next;
        } else {
            current = current.next;
        }
    }
    return dummy.next;
};