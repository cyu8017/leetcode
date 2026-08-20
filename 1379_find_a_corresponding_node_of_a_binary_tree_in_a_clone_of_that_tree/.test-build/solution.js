"use strict";
// LeetCode 1379 - Find A Corresponding Node Of A Binary Tree In A Clone Of That Tree
// https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/
function getTargetCopy(original, cloned, target) {
    const wanted = typeof target === "number" ? target : target.val;
    const stack = [[original, cloned]];
    while (stack.length) {
        const [a, b] = stack.pop();
        if (a.val === wanted)
            return typeof target === "number" ? b.val : b;
        if (a.left)
            stack.push([a.left, b.left]);
        if (a.right)
            stack.push([a.right, b.right]);
    }
}
