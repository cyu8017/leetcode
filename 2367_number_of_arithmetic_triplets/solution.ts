// LeetCode 2367 - Number of Arithmetic Triplets
// https://leetcode.com/problems/number-of-arithmetic-triplets/

export function arithmeticTriplets(nums: number[], diff: number): number {
    const seen = new Set(nums);
    let ans = 0;
    for (const x of nums) {
        if (seen.has(x + diff) && seen.has(x + 2 * diff)) ans++;
    }
    return ans;
}
