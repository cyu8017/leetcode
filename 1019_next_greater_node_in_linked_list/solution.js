// LeetCode 1019 - Next Greater Node In Linked List
// https://leetcode.com/problems/next-greater-node-in-linked-list/

/**
 * @param {number} val
 * @param {ListNode|null} next
 */
function ListNode(val = 0, next = null) {
    this.val = val;
    this.next = next;
}

/**
 * @param {ListNode|null} head
 * @return {number[]}
 */
var nextLargerNodes = function(head) {
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
};
