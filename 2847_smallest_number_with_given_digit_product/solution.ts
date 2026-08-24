// LeetCode 2847 - Smallest Number With Given Digit Product
// https://leetcode.com/problems/smallest-number-with-given-digit-product/

export function smallestNumber(n: number): string {
    if (n === 0) return '0';
    if (n === 1) return '1';
    const digits = [];
    for (let d = 9; d >= 2; d--) {
        while (n % d === 0) {
            digits.push(String(d));
            n = Math.floor(n / d);
        }
    }
    if (n > 1) return '-1';
    return digits.reverse().join('');
}
