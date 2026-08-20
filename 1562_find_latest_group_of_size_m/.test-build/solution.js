"use strict";
// LeetCode 1562 - Find Latest Group of Size M
// https://leetcode.com/problems/find-latest-group-of-size-m/
// @ts-nocheck
function findLatestStep(arr, m) {
    if (m === arr.length)
        return m;
    const lengths = {};
    let answer = -1;
    for (let step = 1; step <= arr.length; step++) {
        const x = arr[step - 1];
        const left = lengths[x - 1] || 0;
        const right = lengths[x + 1] || 0;
        const size = left + 1 + right;
        lengths[x - left] = size;
        lengths[x + right] = size;
        if (left === m || right === m)
            answer = step - 1;
    }
    return answer;
}
