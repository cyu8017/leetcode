// LeetCode 1367 - Linked List In Binary Tree
// https://leetcode.com/problems/linked-list-in-binary-tree/

/**
 * @param {ListNode} head
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSubPath = function(head, root) {
    const match = (a, b) => !a || Boolean(b && a.val === b.val && (match(a.next, b.left) || match(a.next, b.right)));
    return Boolean(root && (match(head, root) || isSubPath(head, root.left) || isSubPath(head, root.right)));
};
