// LeetCode 0163 - Missing Ranges
// https://leetcode.com/problems/missing-ranges/

export function findMissingRanges(
    nums: number[],
    lower: number,
    upper: number,
): number[][] {
    const result: number[][] = [];
    let previous = lower - 1;

    for (const number of [...nums, upper + 1]) {
        if (number - previous >= 2) {
            result.push([previous + 1, number - 1]);
        }
        previous = number;
    }
    return result;
}