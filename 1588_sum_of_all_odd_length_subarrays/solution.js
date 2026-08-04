// LeetCode 1588 - Sum of All Odd Length Subarrays
// https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

/**
 * @param {number[]} arr
 * @return {number}
 */
var sumOddLengthSubarrays = function(arr) {
    const n = arr.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        ans += arr[i] * Math.floor(((i + 1) * (n - i) + 1) / 2);
    }
    return ans;
};
