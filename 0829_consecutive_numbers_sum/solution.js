// LeetCode 0829 - Consecutive Numbers Sum
// https://leetcode.com/problems/consecutive-numbers-sum/

/**
 * @param {number} n
 * @return {number}
 */
var consecutiveNumbersSum = function(n) {
    let ans = 0;
    for (let k = 1; k * (k - 1) / 2 < n; k++) {
        if ((n - k * (k - 1) / 2) % k === 0) ans++;
    }
    return ans;
};
