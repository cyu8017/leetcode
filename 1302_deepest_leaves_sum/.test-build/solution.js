"use strict";
// LeetCode 1302 - Deepest Leaves Sum
// https://leetcode.com/problems/deepest-leaves-sum/
function deepestLeavesSum(root) {
    let level = [root], answer = 0;
    while (level.length) {
        answer = level.reduce((s, n) => s + n.val, 0);
        const next = [];
        for (const node of level) {
            if (node.left)
                next.push(node.left);
            if (node.right)
                next.push(node.right);
        }
        level = next;
    }
    return answer;
}
