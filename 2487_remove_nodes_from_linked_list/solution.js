// LeetCode 2487 - Remove Nodes From Linked List
// https://leetcode.com/problems/remove-nodes-from-linked-list/

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
var removeNodes = function(head) {
    const rev = (node) => {
        let prev = null;
        while (node) {
            const nxt = node.next;
            node.next = prev;
            prev = node;
            node = nxt;
        }
        return prev;
    };
    head = rev(head);
    let mx = 0;
    const dummy = new ListNode(0, head);
    let prev = dummy;
    while (prev.next) {
        if (prev.next.val >= mx) {
            mx = prev.next.val;
            prev = prev.next;
        } else {
            prev.next = prev.next.next;
        }
    }
    return rev(dummy.next);
};
