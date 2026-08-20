"use strict";
// LeetCode 1536 - Minimum Swaps to Arrange a Binary Grid
// https://leetcode.com/problems/minimum-swaps-to-arrange-a-binary-grid/
// @ts-nocheck
function minSwaps(grid) {
    const zeros = [];
    for (const row of grid) {
        let count = 0;
        for (let i = row.length - 1; i >= 0; i--) {
            if (row[i])
                break;
            count++;
        }
        zeros.push(count);
    }
    let answer = 0;
    const n = grid.length;
    for (let i = 0; i < n; i++) {
        const required = n - i - 1;
        let j = i;
        while (j < n && zeros[j] < required)
            j++;
        if (j === n)
            return -1;
        answer += j - i;
        const val = zeros[j];
        zeros.splice(j, 1);
        zeros.splice(i, 0, val);
    }
    return answer;
}
