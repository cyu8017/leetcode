class ListNode {
    val: number;
    next: ListNode | null;

    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

export function plusOne(head: ListNode | null): ListNode | null {
    const sentinel = new ListNode(0, head);
    let notNine: ListNode = sentinel;
    let node = head;

    while (node) {
        if (node.val !== 9) notNine = node;
        node = node.next;
    }

    notNine.val += 1;
    node = notNine.next;
    while (node) {
        node.val = 0;
        node = node.next;
    }

    return sentinel.val === 1 ? sentinel : sentinel.next;
}
