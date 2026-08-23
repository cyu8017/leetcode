// LeetCode 0092 - Reverse Linked List II
// https://leetcode.com/problems/reverse-linked-list-ii/

function ListNode(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
var reverseBetween = function(head, left, right) {
    if (!head || left === right) {
        return head;
    }

    const dummy = new ListNode(0, head);
    let before = dummy;
    for (let i = 0; i < left - 1; i++) {
        before = before.next;
    }

    const start = before.next;
    let current = start.next;

    for (let i = 0; i < right - left; i++) {
        start.next = current.next;
        current.next = before.next;
        before.next = current;
        current = start.next;
    }

    return dummy.next;
};
