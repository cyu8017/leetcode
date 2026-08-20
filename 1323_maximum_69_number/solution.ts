// LeetCode 1323 - Maximum 69 Number
// https://leetcode.com/problems/maximum-69-number/

function maximum69Number(num: number): number {
    return Number(String(num).replace("6", "9"));
}
