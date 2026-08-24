// LeetCode 3217 - Delete Nodes From Linked List Present in Array
// https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/

export function modifiedList(nums: any, head: any): any {
    const s = new Set(nums);
    const dummy = { val: 0, next: head };
    for (let pre = dummy; pre.next !== null; ) {
        if (s.has(pre.next.val)) pre.next = pre.next.next;
        else pre = pre.next;
    }
    return dummy.next;
}
