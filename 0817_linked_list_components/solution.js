// LeetCode 0817 - Linked List Components
// https://leetcode.com/problems/linked-list-components/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number[]} nums
 * @return {number}
 */
var numComponents = function(head, nums) {
    const present = new Set(nums);
    let count = 0, connected = false;
    while (head) {
        if (present.has(head.val)) {
            if (!connected) {
                count++;
                connected = true;
            }
        } else {
            connected = false;
        }
        head = head.next;
    }
    return count;
};
