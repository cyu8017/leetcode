// LeetCode 1281 - Subtract the Product and Sum of Digits of an Integer
// https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

function subtractProductAndSum(n: number): number {
    let product = 1;
    let total = 0;
    while (n > 0) {
        const digit = n % 10;
        product *= digit;
        total += digit;
        n = Math.floor(n / 10);
    }
    return product - total;
}
