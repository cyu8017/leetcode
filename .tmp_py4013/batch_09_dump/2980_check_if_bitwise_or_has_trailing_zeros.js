// LeetCode 2980 - Check if Bitwise OR Has Trailing Zeros
// https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/

var hasTrailingZeros = function(nums) {
    let even = 0;
    for (const v of nums) {
        if (v % 2 === 0) {
            even++;
            if (even >= 2) return true;
        }
    }
    return false;
};
