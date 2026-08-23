// LeetCode 0025 - Reverse Nodes in k-Group
// https://leetcode.com/problems/reverse-nodes-in-k-group/

function ListNode(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function(head, k) {
    const dummy = new ListNode(0, head);
    let groupPrevious = dummy;

    while (true) {
        let kth = groupPrevious;
        for (let i = 0; i < k; i++) {
            kth = kth.next;
            if (!kth) {
                return dummy.next;
            }
        }

        const groupNext = kth.next;
        let previous = groupNext;
        let current = groupPrevious.next;

        while (current !== groupNext) {
            const next = current.next;
            current.next = previous;
            previous = current;
            current = next;
        }

        const tmp = groupPrevious.next;
        groupPrevious.next = kth;
        groupPrevious = tmp;
    }
};
