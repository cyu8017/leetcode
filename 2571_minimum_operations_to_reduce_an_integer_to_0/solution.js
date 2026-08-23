// LeetCode 2571 - Minimum Operations to Reduce an Integer to 0
// https://leetcode.com/problems/minimum-operations-to-reduce-an-integer-to-0/

/**
 * @param {number} n
 * @return {number}
 */
var minOperations = function(n) {
    let ans = 0;
    while (n > 0) {
        if ((n & 3) === 3) {
            n++;
            ans++;
        } else if ((n & 1) !== 0) {
            n--;
            ans++;
        } else {
            n >>= 1;
        }
    }
    return ans;
};
