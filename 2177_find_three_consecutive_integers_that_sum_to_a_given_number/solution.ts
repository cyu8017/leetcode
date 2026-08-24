// LeetCode 2177 - Find Three Consecutive Integers That Sum to a Given Number
// https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/

export function sumOfThree(num: number): number[] {
    if (num % 3 !== 0) return [];
    const x = Math.floor(num / 3);
    return [x - 1, x, x + 1];
}
