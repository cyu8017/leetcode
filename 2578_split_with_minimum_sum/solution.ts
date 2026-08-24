// LeetCode 2578 - Split With Minimum Sum
// https://leetcode.com/problems/split-with-minimum-sum/

export function splitNum(num: number): number {
    const digits = [];
    while (num > 0) {
        digits.push(num % 10);
        num = Math.floor(num / 10);
    }
    digits.sort((a, b) => a - b);
    let a = 0, b = 0;
    for (let i = 0; i < digits.length; ++i) {
        if (i % 2 === 0) a = a * 10 + digits[i];
        else b = b * 10 + digits[i];
    }
    return a + b;
}
