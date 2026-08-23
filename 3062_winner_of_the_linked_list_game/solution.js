// LeetCode 3062 - Winner of the Linked List Game
// https://leetcode.com/problems/winner-of-the-linked-list-game/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {string}
 */
var gameResult = function(head) {
    let odd = 0, even = 0;
    for (; head !== null; head = head.next.next) {
        const a = head.val, b = head.next.val;
        if (a < b) odd++;
        if (a > b) even++;
    }
    if (odd > even) return "Odd";
    if (odd < even) return "Even";
    return "Tie";
};
