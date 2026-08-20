"use strict";
// LeetCode 1504 - Count Submatrices With All Ones
// https://leetcode.com/problems/count-submatrices-with-all-ones/
// @ts-nocheck
function numSubmat(mat) {
    let ans = 0;
    const heights = Array(mat[0].length).fill(0);
    for (const row of mat) {
        for (let j = 0; j < row.length; j++) {
            heights[j] = row[j] ? heights[j] + 1 : 0;
        }
        const stack = [];
        let running = 0;
        for (const h of heights) {
            let count = 1;
            while (stack.length && stack[stack.length - 1][0] >= h) {
                const [old, width] = stack.pop();
                running -= old * width;
                count += width;
            }
            stack.push([h, count]);
            running += h * count;
            ans += running;
        }
    }
    return ans;
}
