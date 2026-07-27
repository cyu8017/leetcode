// LeetCode 1669 - Merge In Between Linked Lists
// https://leetcode.com/problems/merge-in-between-linked-lists/

/**
 * @param {object} list1
 * @param {number} a
 * @param {number} b
 * @param {object} list2
 * @return {object}
 */
var mergeInBetween = function(list1, a, b, list2) {
    let pre = list1;
    for (let i = 0; i < a - 1; i++) pre = pre.next;
    let post = pre;
    for (let i = 0; i < b - a + 2; i++) post = post.next;
    pre.next = list2;
    while (pre.next) pre = pre.next;
    pre.next = post;
    return list1;
};
