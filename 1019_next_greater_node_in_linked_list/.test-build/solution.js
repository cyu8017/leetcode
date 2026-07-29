"use strict";
// LeetCode 1019 - Next Greater Node In Linked List
// https://leetcode.com/problems/next-greater-node-in-linked-list/
function nextLargerNodes(head) {
    const vals = [];
    while (head) {
        vals.push(head.val);
        head = head.next;
    }
    const ans = new Array(vals.length).fill(0);
    const stack = [];
    for (let i = 0; i < vals.length; i++) {
        while (stack.length && vals[stack[stack.length - 1]] < vals[i]) {
            ans[stack.pop()] = vals[i];
        }
        stack.push(i);
    }
    return ans;
}
