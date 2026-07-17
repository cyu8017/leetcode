// LeetCode 1748 - Sum of Unique Elements
// https://leetcode.com/problems/sum-of-unique-elements/

function sumOfUnique(nums: number[]): number {
    const counts = new Map<number, number>();
    for (const value of nums) {
        counts.set(value, (counts.get(value) || 0) + 1);
    }
    let total = 0;
    for (const [value, count] of counts) {
        if (count === 1) {
            total += value;
        }
    }
    return total;
}
