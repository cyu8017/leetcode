// LeetCode 0978 - Longest Turbulent Subarray
// https://leetcode.com/problems/longest-turbulent-subarray/

/**
 * @param {number[]} arr
 * @return {number}
 */
var maxTurbulenceSize = function(arr) {
    let ans = 1, cur = 1;
    for (let i = 1; i < arr.length; i++) {
        if (arr[i] === arr[i - 1]) cur = 1;
        else if (i === 1 || (arr[i] - arr[i - 1]) * (arr[i - 1] - arr[i - 2]) < 0) cur++;
        else cur = 2;
        ans = Math.max(ans, cur);
    }
    return ans;
};
