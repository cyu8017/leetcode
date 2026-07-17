"use strict";
// LeetCode 1713 - Minimum Operations to Make a Subsequence
// https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/
function minOperations(target, arr) {
    const pos = new Map();
    target.forEach((value, i) => pos.set(value, i));
    const lis = [];
    for (const value of arr) {
        if (!pos.has(value)) {
            continue;
        }
        const idx = pos.get(value);
        let lo = 0;
        let hi = lis.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (lis[mid] < idx) {
                lo = mid + 1;
            }
            else {
                hi = mid;
            }
        }
        if (lo === lis.length) {
            lis.push(idx);
        }
        else {
            lis[lo] = idx;
        }
    }
    return target.length - lis.length;
}
