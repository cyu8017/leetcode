// LeetCode 1265 - Print Immutable Linked List in Reverse
// https://leetcode.com/problems/print-immutable-linked-list-in-reverse/

/**
 * @param {ImmutableListNode} head
 * @return {void}
 */
var printLinkedListInReverse = function(head) {
    if (!head) return;
    printLinkedListInReverse(head.getNext());
    head.printValue();
};
