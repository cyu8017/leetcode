// LeetCode 1134 - Armstrong Number
// https://leetcode.com/problems/armstrong-number/

function isArmstrong(n: number): boolean {
    const digits = String(n);
    const power = digits.length;
    let sum = 0;
    for (const d of digits) sum += Number(d) ** power;
    return n === sum;
}
