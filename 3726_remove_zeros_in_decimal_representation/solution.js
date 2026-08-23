// LeetCode 3726 - Remove Zeros in Decimal Representation
// https://leetcode.com/problems/remove-zeros-in-decimal-representation/

var removeZeros = function(n) {
    let ans = 0, k = 1;
    while (n > 0) {
        const x = n % 10;
        if (x > 0) {
            ans = k * x + ans;
            k *= 10;
        }
        n = Math.floor(n / 10);
    }
    return ans;
};
