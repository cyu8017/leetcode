// LeetCode 1085 - Sum of Digits in the Minimum Number
// https://leetcode.com/problems/sum-of-digits-in-the-minimum-number/

function sumOfDigits(nums: number[]): number {
    let n = Math.min(...nums);
    let digitSum = 0;
    while (n) {
        digitSum += n % 10;
        n = Math.floor(n / 10);
    }
    return digitSum % 2 === 0 ? 1 : 0;
}
