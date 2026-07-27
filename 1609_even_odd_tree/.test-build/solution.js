"use strict";
// LeetCode 1609 - Even Odd Tree
// https://leetcode.com/problems/even-odd-tree/
function isEvenOddTree(root) {
    let q = root ? [root] : [];
    let level = 0;
    while (q.length) {
        let prev = level % 2 === 0 ? -Infinity : Infinity;
        const nxt = [];
        for (const node of q) {
            if (node.val % 2 === level % 2)
                return false;
            if (level % 2 === 0 && node.val <= prev)
                return false;
            if (level % 2 === 1 && node.val >= prev)
                return false;
            prev = node.val;
            if (node.left)
                nxt.push(node.left);
            if (node.right)
                nxt.push(node.right);
        }
        q = nxt;
        level++;
    }
    return true;
}
