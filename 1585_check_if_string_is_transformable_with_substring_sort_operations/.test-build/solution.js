"use strict";
// LeetCode 1585 - Check If String Is Transformable With Substring Sort Operations
// https://leetcode.com/problems/check-if-string-is-transformable-with-substring-sort-operations/
// @ts-nocheck
function isTransformable(s, t) {
    const positions = Array.from({ length: 10 }, () => []);
    for (let i = 0; i < s.length; i++)
        positions[+s[i]].push(i);
    const heads = Array(10).fill(0);
    for (const ch of t) {
        const d = +ch;
        if (heads[d] >= positions[d].length)
            return false;
        const index = positions[d][heads[d]];
        for (let smaller = 0; smaller < d; smaller++) {
            if (heads[smaller] < positions[smaller].length && positions[smaller][heads[smaller]] < index) {
                return false;
            }
        }
        heads[d]++;
    }
    return true;
}
