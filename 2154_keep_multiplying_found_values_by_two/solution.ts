// LeetCode 2154 - Keep Multiplying Found Values by Two
// https://leetcode.com/problems/keep-multiplying-found-values-by-two/

export function findFinalValue(nums: number[], original: number): number {
    const have = new Set(nums);
    while (have.has(original)) original *= 2;
    return original;
}
