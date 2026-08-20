// LeetCode 1295 - Find Numbers with Even Number of Digits
// https://leetcode.com/problems/find-numbers-with-even-number-of-digits/

function findNumbers(nums: number[]): number {
    return nums.reduce((count, value) => {
        const digits = value === 0 ? 1 : Math.floor(Math.log10(Math.abs(value))) + 1;
        return count + (digits % 2 === 0 ? 1 : 0);
    }, 0);
}
