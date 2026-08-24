// LeetCode 0707 - Design Linked List
// https://leetcode.com/problems/design-linked-list/

export class MyLinkedList {
    constructor() {
        this.dummy = { val: 0, next: null };
        this.size = 0;
    }

    get(index: any): any {
        if (index < 0 || index >= this.size) return -1;
        let node = this.dummy.next;
        for (let i = 0; i < index; i++) node = node.next;
        return node.val;
    }

    addAtHead(val: any): any { this.addAtIndex(0, val); }

    addAtTail(val: any): any { this.addAtIndex(this.size, val); }

    addAtIndex(index: any, val: any): any {
        if (index < 0 || index > this.size) return;
        let prev = this.dummy;
        for (let i = 0; i < index; i++) prev = prev.next;
        const node = { val, next: prev.next };
        prev.next = node;
        this.size++;
    }

    deleteAtIndex(index: any): any {
        if (index < 0 || index >= this.size) return;
        let prev = this.dummy;
        for (let i = 0; i < index; i++) prev = prev.next;
        prev.next = prev.next.next;
        this.size--;
    }
}
