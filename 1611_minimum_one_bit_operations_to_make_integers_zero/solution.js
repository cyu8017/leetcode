// LeetCode 1611 - Minimum One Bit Operations to Make Integers Zero
// https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/

/**
 * @param {number} n
 * @return {number}
 */
var minimumOneBitOperations = function(n) {
    let ans = 0;
    while (n) {
        ans ^= n;
        n >>= 1;
    }
    return ans;
};
