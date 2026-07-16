// LeetCode 0263 - Ugly Number
// https://leetcode.com/problems/ugly-number/

export function isUgly(n: number): boolean {
    if (n <= 0) {
        return false;
    }
    for (const factor of [2, 3, 5]) {
        while (n % factor === 0) {
            n = Math.floor(n / factor);
        }
    }
    return n === 1;
}
