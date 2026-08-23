// LeetCode 0061 - Rotate List
// https://leetcode.com/problems/rotate-list/

function ListNode(val, next) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
}

/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var rotateRight = function(head, k) {
    if (!head || !head.next) {
        return head;
    }

    let tail = head;
    let length = 1;
    while (tail.next) {
        tail = tail.next;
        length += 1;
    }

    tail.next = head;
    k %= length;
    if (k === 0) {
        tail.next = null;
        return head;
    }

    const steps = length - k;
    let newTail = head;
    for (let i = 0; i < steps - 1; i++) {
        newTail = newTail.next;
    }

    const newHead = newTail.next;
    newTail.next = null;
    return newHead;
};
