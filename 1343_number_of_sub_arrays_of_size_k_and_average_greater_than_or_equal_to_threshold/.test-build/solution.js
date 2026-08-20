"use strict";
// LeetCode 1343 - Number Of Sub Arrays Of Size K And Average Greater Than Or Equal To Threshold
// https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
function numOfSubarrays(arr, k, threshold) {
    let window = 0;
    for (let i = 0; i < k; i++)
        window += arr[i];
    let answer = window >= k * threshold ? 1 : 0;
    for (let i = k; i < arr.length; i++) {
        window += arr[i] - arr[i - k];
        if (window >= k * threshold)
            answer++;
    }
    return answer;
}
