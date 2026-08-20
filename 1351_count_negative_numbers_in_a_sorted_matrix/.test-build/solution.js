"use strict";
// LeetCode 1351 - Count Negative Numbers In A Sorted Matrix
// https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
function countNegatives(grid) {
    let answer = 0;
    for (const row of grid) {
        let lo = 0, hi = row.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (row[mid] < 0)
                hi = mid;
            else
                lo = mid + 1;
        }
        answer += row.length - lo;
    }
    return answer;
}
