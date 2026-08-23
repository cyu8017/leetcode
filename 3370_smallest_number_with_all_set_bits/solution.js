// LeetCode 3370 - Smallest Number With All Set Bits
// https://leetcode.com/problems/smallest-number-with-all-set-bits/

var smallestNumber = function(n) {
    let x = 1;
    while (x < n) x = x * 2 + 1;
    return x;
};
