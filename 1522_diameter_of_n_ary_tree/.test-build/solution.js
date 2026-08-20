"use strict";
// LeetCode 1522 - Diameter of N-Ary Tree
// https://leetcode.com/problems/diameter-of-n-ary-tree/
// @ts-nocheck
function diameter(root) {
    let answer = 0;
    const depth = (node) => {
        let longest = 0, second = 0;
        for (const child of node.children || []) {
            const value = depth(child) + 1;
            if (value > longest) {
                second = longest;
                longest = value;
            }
            else if (value > second)
                second = value;
        }
        answer = Math.max(answer, longest + second);
        return longest;
    };
    if (root)
        depth(root);
    return answer;
}
