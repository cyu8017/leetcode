// LeetCode 1290 - Convert Binary Number in a Linked List to Integer
// https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

/**
 * @param {ListNode} head
 * @return {number}
 */
var getDecimalValue = function(head) {
    let value = 0;
    while (head) {
        value = value * 2 + head.val;
        head = head.next;
    }
    return value;
};
