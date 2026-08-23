// LeetCode 3622 - Check Divisibility by Digit Sum and Product
// https://leetcode.com/problems/check-divisibility-by-digit-sum-and-product/

var checkDivisibility = function(n) {
    let s = 0, p = 1, x = n;
    while (x !== 0) {
        const v = x % 10;
        x = Math.floor(x / 10);
        s += v;
        p *= v;
    }
    return n % (s + p) === 0;
};
