export class ListNode {
    val: number;
    next: ListNode | null;
    constructor(val?: number, next?: ListNode | null) {
        this.val = val ?? 0;
        this.next = next ?? null;
    }
}

export function oddEvenList(head: ListNode | null): ListNode | null {
    if (!head || !head.next) return head;
    let odd: ListNode = head;
    let even: ListNode | null = head.next;
    const evenHead = even;
    while (even && even.next) {
        odd.next = even.next;
        odd = odd.next;
        even.next = odd.next;
        even = even.next;
    }
    odd.next = evenHead;
    return head;
}
