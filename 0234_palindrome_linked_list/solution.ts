// LeetCode 0234 - Palindrome Linked List
// https://leetcode.com/problems/palindrome-linked-list/

export class ListNode {
    val: number;
    next: ListNode | null;

    constructor(val = 0, next: ListNode | null = null) {
        this.val = val;
        this.next = next;
    }
}

export function isPalindrome(head: ListNode | null): boolean {
    if (!head || !head.next) {
        return true;
    }

    let slow: ListNode | null = head;
    let fast: ListNode | null = head;
    while (fast && fast.next) {
        slow = slow!.next;
        fast = fast.next.next;
    }

    let prev: ListNode | null = null;
    while (slow) {
        const next = slow.next;
        slow.next = prev;
        prev = slow;
        slow = next;
    }

    let left: ListNode | null = head;
    let right: ListNode | null = prev;
    while (right) {
        if (left!.val !== right.val) {
            return false;
        }
        left = left!.next;
        right = right.next;
    }
    return true;
}
