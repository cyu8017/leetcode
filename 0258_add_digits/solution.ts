// LeetCode 0258 - Add Digits
// https://leetcode.com/problems/add-digits/

export function addDigits(num: number): number {
    if (num === 0) {
        return 0;
    }
    return 1 + ((num - 1) % 9);
}
