// LeetCode 2261 - K Divisible Elements Subarrays
// https://leetcode.com/problems/k-divisible-elements-subarrays/

export function countDistinct(nums: number[], k: number, p: number): number {
    const n = nums.length;
    const seen = new Set();
    for (let i = 0; i < n; i++) {
        let div = 0, key = '';
        for (let j = i; j < n; j++) {
            if (nums[j] % p === 0) div++;
            if (div > k) break;
            key += (nums[j] + 1) + ',';
            seen.add(key);
        }
    }
    return seen.size;
}
