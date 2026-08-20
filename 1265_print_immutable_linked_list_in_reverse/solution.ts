// LeetCode 1265 - Print Immutable Linked List in Reverse
// https://leetcode.com/problems/print-immutable-linked-list-in-reverse/

interface ImmutableListNode {
    printValue(): void;
    getNext(): ImmutableListNode | null;
}

function printLinkedListInReverse(head: ImmutableListNode | null): void {
    if (!head) return;
    printLinkedListInReverse(head.getNext());
    head.printValue();
}
