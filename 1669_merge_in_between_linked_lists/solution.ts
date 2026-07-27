// LeetCode 1669 - Merge In Between Linked Lists
// https://leetcode.com/problems/merge-in-between-linked-lists/

interface ListNode1669 {
    val: number;
    next: ListNode1669 | null;
}

function mergeInBetween(list1: ListNode1669, a: number, b: number, list2: ListNode1669): ListNode1669 {
    let pre: ListNode1669 = list1;
    for (let i = 0; i < a - 1; i++) pre = pre.next!;
    let post: ListNode1669 | null = pre;
    for (let i = 0; i < b - a + 2; i++) post = post!.next;
    pre.next = list2;
    while (pre.next) pre = pre.next;
    pre.next = post;
    return list1;
}
