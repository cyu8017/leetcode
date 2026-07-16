// LeetCode 0430 - Flatten a Multilevel Doubly Linked List
// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

export class Node {
    val: number;
    prev: Node | null;
    next: Node | null;
    child: Node | null;

    constructor(val: number = 0, prev: Node | null = null, next: Node | null = null, child: Node | null = null) {
        this.val = val;
        this.prev = prev;
        this.next = next;
        this.child = child;
    }
}

export class Solution {
    flatten(head: Node | null): Node | null {
        let current = head;
        while (current) {
            if (current.child) {
                const nextNode = current.next;
                const childHead = this.flatten(current.child);
                current.next = childHead;
                if (childHead) childHead.prev = current;
                let tail = childHead;
                while (tail && tail.next) {
                    tail = tail.next;
                }
                if (tail) {
                    tail.next = nextNode;
                    if (nextNode) nextNode.prev = tail;
                }
                current.child = null;
            }
            current = current.next;
        }
        return head;
    }
}
