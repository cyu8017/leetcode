// LeetCode 0708 - Insert into a Sorted Circular Linked List
// https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

/**
 * @param {Node} head
 * @param {number} insertVal
 * @return {Node}
 */
var insert = function(head, insertVal) {
    const node = new Node(insertVal);
    if (head === null) {
        node.next = node;
        return node;
    }
    let cur = head;
    while (cur.next !== null && cur.next !== head) cur = cur.next;
    cur.next = head;
    let prev = head, curr = head.next;
    while (true) {
        if (prev.val <= insertVal && insertVal <= curr.val) break;
        if (prev.val > curr.val && (insertVal >= prev.val || insertVal <= curr.val)) break;
        prev = curr;
        curr = curr.next;
        if (prev === head) break;
    }
    prev.next = node;
    node.next = curr;
    return head;
};
