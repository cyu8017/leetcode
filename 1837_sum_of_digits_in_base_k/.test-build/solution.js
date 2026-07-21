"use strict";
// LeetCode 1837 - Sum of Digits in Base K
// https://leetcode.com/problems/sum-of-digits-in-base-k/
function sumBase(n, k) {
    let total = 0;
    while (n) {
        total += n % k;
        n = Math.floor(n / k);
    }
    return total;
}
