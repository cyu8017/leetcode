// LeetCode 0234 - Palindrome Linked List
// https://leetcode.com/problems/palindrome-linked-list/

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
 * @return {boolean}
 */
var isPalindrome = function(head) {
    if (!head || !head.next) {
        return true;
    }

    let slow = head;
    let fast = head;
    while (fast && fast.next) {
        slow = slow.next;
        fast = fast.next.next;
    }

    let prev = null;
    while (slow) {
        const next = slow.next;
        slow.next = prev;
        prev = slow;
        slow = next;
    }

    let left = head;
    let right = prev;
    while (right) {
        if (left.val !== right.val) {
            return false;
        }
        left = left.next;
        right = right.next;
    }
    return true;
};
