// LeetCode 0138 - Copy List with Random Pointer
// https://leetcode.com/problems/copy-list-with-random-pointer/

export class Node {
    val: number;
    next: Node | null;
    random: Node | null;

    constructor(val = 0, next: Node | null = null, random: Node | null = null) {
        this.val = val;
        this.next = next;
        this.random = random;
    }
}

export function copyRandomList(head: Node | null): Node | null {
    const clones = new Map<Node, Node>();

    const clone = (node: Node | null): Node | null => {
        if (!node) return null;

        const existing = clones.get(node);
        if (existing) return existing;

        const copy = new Node(node.val);
        clones.set(node, copy);
        copy.next = clone(node.next);
        copy.random = clone(node.random);
        return copy;
    };

    return clone(head);
}