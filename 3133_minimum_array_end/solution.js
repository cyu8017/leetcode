// LeetCode 3133 - Minimum Array End
// https://leetcode.com/problems/minimum-array-end/

/**
 * @param {number} n
 * @param {number} x
 * @return {number}
 */
var minEnd = function(n, x) {
    n--;
    let ans = BigInt(x);
    for (let i = 0; i < 31; i++) {
        if (((x >> i) & 1) === 0) {
            ans |= BigInt(n & 1) << BigInt(i);
            n >>= 1;
        }
    }
    ans |= BigInt(n) << 31n;
    return Number(ans);
};
