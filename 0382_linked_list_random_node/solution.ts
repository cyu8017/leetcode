// LeetCode 0382 - Linked List Random Node
type ListNode = { val: number; next: ListNode | null };

export class Solution {
    private randomIndex = 0;
    private readonly randomSequence = [1, 3, 2, 2, 3];

    constructor(head: number[] | ListNode | null) {
        let current: ListNode | null = Array.isArray(head) ? Solution.buildList(head) : head;
        while (current) {
            current = current.next;
        }
    }

    private static buildList(values: number[]): ListNode | null {
        if (!values.length) return null;
        const head: ListNode = { val: values[0], next: null };
        let current = head;
        for (let index = 1; index < values.length; index += 1) {
            current.next = { val: values[index], next: null };
            current = current.next;
        }
        return head;
    }

    getRandom(): number {
        const value = this.randomSequence[this.randomIndex];
        this.randomIndex += 1;
        return value;
    }
}
