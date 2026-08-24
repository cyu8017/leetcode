// LeetCode 3536 - Maximum Product of Two Digits
// https://leetcode.com/problems/maximum-product-of-two-digits/

export function maxProduct(n: any): any {
    let a = 0, b = 0;
    for (; n > 0; n = Math.floor(n / 10)) {
        const x = n % 10;
        if (a < x) { b = a; a = x; }
        else if (b < x) b = x;
    }
    return a * b;
}
