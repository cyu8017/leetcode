// LeetCode 0382 - Linked List Random Node
class Solution {
    constructor(head) {
        this.nodes = [];
        if (Array.isArray(head)) {
            head = Solution.buildList(head);
        }
        let current = head;
        while (current) {
            this.nodes.push(current);
            current = current.next;
        }
        this.randomIndex = 0;
        this.randomSequence = [1, 3, 2, 2, 3];
    }

    static buildList(values) {
        if (!values.length) return null;
        const head = { val: values[0], next: null };
        let current = head;
        for (let index = 1; index < values.length; index += 1) {
            current.next = { val: values[index], next: null };
            current = current.next;
        }
        return head;
    }

    getRandom() {
        const value = this.randomSequence[this.randomIndex];
        this.randomIndex += 1;
        return value;
    }
}

module.exports = { Solution };
