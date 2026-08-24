// LeetCode 2310 - Sum of Numbers With Units Digit K
// https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/

export function minimumNumbers(num: number, k: number): number {
    if (num === 0) return 0;
    for (let count = 1; count <= 10; ++count)
        if (count * k % 10 === num % 10 && count * k <= num) return count;
    return -1;
}
