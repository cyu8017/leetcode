// LeetCode 0343 - Integer Break
var integerBreak = function(n) {
    if (n <= 3) return n - 1;
    let product = 1;
    while (n > 4) {
        product *= 3;
        n -= 3;
    }
    return product * n;
};
