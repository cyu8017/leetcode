"use strict";
// LeetCode 1574 - Shortest Subarray to be Removed to Make Array Sorted
// https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
// @ts-nocheck
function findLengthOfShortestSubarray(arr) {
    const n = arr.length;
    let right = n - 1;
    while (right && arr[right - 1] <= arr[right])
        right--;
    if (right === 0)
        return 0;
    let answer = right, left = 0;
    while (left === 0 || (left < n && arr[left - 1] <= arr[left])) {
        while (right < n && arr[right] < arr[left])
            right++;
        answer = Math.min(answer, right - left - 1);
        left++;
        if (left >= n)
            break;
    }
    return answer;
}
