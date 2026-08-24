// LeetCode 0633 - Sum of Square Numbers
// https://leetcode.com/problems/sum-of-square-numbers/

export function judgeSquareSum(c: number): boolean {
    let left = 0;
    let right = Math.floor(Math.sqrt(c));
    while (left <= right) {
        const total = left * left + right * right;
        if (total === c) return true;
        if (total < c) ++left;
        else --right;
    }
    return false;
}
