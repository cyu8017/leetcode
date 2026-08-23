// LeetCode 0707 - Design Linked List
// https://leetcode.com/problems/design-linked-list/

class MyLinkedList {
    constructor() {
        this.dummy = { val: 0, next: null };
        this.size = 0;
    }

    /**
     * @param {number} index
     * @return {number}
     */
    get(index) {
        if (index < 0 || index >= this.size) return -1;
        let node = this.dummy.next;
        for (let i = 0; i < index; i++) node = node.next;
        return node.val;
    }

    /**
     * @param {number} val
     * @return {void}
     */
    addAtHead(val) { this.addAtIndex(0, val); }

    /**
     * @param {number} val
     * @return {void}
     */
    addAtTail(val) { this.addAtIndex(this.size, val); }

    /**
     * @param {number} index
     * @param {number} val
     * @return {void}
     */
    addAtIndex(index, val) {
        if (index < 0 || index > this.size) return;
        let prev = this.dummy;
        for (let i = 0; i < index; i++) prev = prev.next;
        const node = { val, next: prev.next };
        prev.next = node;
        this.size++;
    }

    /**
     * @param {number} index
     * @return {void}
     */
    deleteAtIndex(index) {
        if (index < 0 || index >= this.size) return;
        let prev = this.dummy;
        for (let i = 0; i < index; i++) prev = prev.next;
        prev.next = prev.next.next;
        this.size--;
    }
}
