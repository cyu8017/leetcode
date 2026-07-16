// LeetCode 0430 - Flatten a Multilevel Doubly Linked List
// https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

class Node {
    constructor(val = 0, prev = null, next = null, child = null) {
        this.val = val;
        this.prev = prev;
        this.next = next;
        this.child = child;
    }
}

class Solution {
    flatten(head) {
        let current = head;
        while (current) {
            if (current.child) {
                const nextNode = current.next;
                const childHead = this.flatten(current.child);
                current.next = childHead;
                childHead.prev = current;
                let tail = childHead;
                while (tail.next) {
                    tail = tail.next;
                }
                tail.next = nextNode;
                if (nextNode) {
                    nextNode.prev = tail;
                }
                current.child = null;
            }
            current = current.next;
        }
        return head;
    }
}

module.exports = { Solution, Node };
