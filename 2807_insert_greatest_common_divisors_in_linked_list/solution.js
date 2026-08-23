// LeetCode 2807 - Insert Greatest Common Divisors in Linked List
// https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var insertGreatestCommonDivisors = function(head) {
    const gcd = (a, b) => {
        while (b) { const t = a % b; a = b; b = t; }
        return a;
    };
    let cur = head;
    while (cur && cur.next) {
        const g = gcd(cur.val, cur.next.val);
        const node = new ListNode(g, cur.next);
        cur.next = node;
        cur = node.next;
    }
    return head;
};
