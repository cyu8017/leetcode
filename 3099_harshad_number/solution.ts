// LeetCode 3099 - Harshad Number
// https://leetcode.com/problems/harshad-number/

export function sumOfTheDigitsOfHarshadNumber(x: number): number {
    let s = 0;
    for (let y = x; y > 0; y = Math.floor(y / 10)) s += y % 10;
    return x % s === 0 ? s : -1;
}
