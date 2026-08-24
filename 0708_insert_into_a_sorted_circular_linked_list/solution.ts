// LeetCode 0708 - Insert into a Sorted Circular Linked List
// https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/

class Node {
    val: number;
    children: Node[];
    constructor(val?: number, children?: Node[]) {
        this.val = val ?? 0;
        this.children = children ?? [];
    }
}

export function insert(head: Node | null, insertVal: number): Node | null {
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
}
