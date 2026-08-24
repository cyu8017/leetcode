// LeetCode 3063 - Linked List Frequency
// https://leetcode.com/problems/linked-list-frequency/

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
var frequenciesOfElements = function(head) {
    const cnt = new Map();
    for (; head !== null; head = head.next)
        cnt.set(head.val, (cnt.get(head.val) || 0) + 1);
    let dummy = { val: 0, next: null };
    for (const val of cnt.values())
        dummy.next = { val, next: dummy.next };
    return dummy.next;
};
