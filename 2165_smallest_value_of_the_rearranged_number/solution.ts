// LeetCode 2165 - Smallest Value of the Rearranged Number
// https://leetcode.com/problems/smallest-value-of-the-rearranged-number/

export function smallestNumber(num: number): number {
    let neg = num < 0;
    if (neg) num = -num;
    if (num === 0) return 0;
    const digits = [];
    while (num > 0) { digits.push(num % 10); num = Math.floor(num / 10); }
    if (neg) {
        digits.sort((a, b) => b - a);
        let ans = 0;
        for (const d of digits) ans = ans * 10 + d;
        return -ans;
    }
    digits.sort((a, b) => a - b);
    if (digits[0] === 0) {
        for (let i = 1; i < digits.length; i++) {
            if (digits[i] !== 0) {
                const t = digits[0]; digits[0] = digits[i]; digits[i] = t;
                break;
            }
        }
    }
    let res = 0;
    for (const d of digits) res = res * 10 + d;
    return res;
}
