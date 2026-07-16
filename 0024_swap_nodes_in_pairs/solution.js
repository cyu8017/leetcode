// LeetCode 0024 - Swap Nodes in Pairs
// https://leetcode.com/problems/swap-nodes-in-pairs/

function ListNode(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var swapPairs = function(head) {
    const dummy = new ListNode(0, head);
    let previous = dummy;

    while (previous.next && previous.next.next) {
        const first = previous.next;
        const second = previous.next.next;
        first.next = second.next;
        second.next = first;
        previous.next = second;
        previous = first;
    }

    return dummy.next;
};
