// LeetCode 1171 - Remove Zero Sum Consecutive Nodes from Linked List
// https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var removeZeroSumSublists = function(head) {
    const dummy = { val: 0, next: head };
    let prefix = 0;
    const seen = new Map([[0, dummy]]);
    let node = dummy;
    while (node) {
        prefix += node.val;
        seen.set(prefix, node);
        node = node.next;
    }
    prefix = 0;
    node = dummy;
    while (node) {
        prefix += node.val;
        node.next = seen.get(prefix).next;
        node = node.next;
    }
    return dummy.next;
};
