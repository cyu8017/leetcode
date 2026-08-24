// LeetCode 2537 - Count the Number of Good Subarrays
// https://leetcode.com/problems/count-the-number-of-good-subarrays/

export function countGood(nums: number[], k: number): number {
    const freq = new Map();
    let pairs = 0, ans = 0, left = 0;
    for (let right = 0; right < nums.length; right++) {
        pairs += freq.get(nums[right]) || 0;
        freq.set(nums[right], (freq.get(nums[right]) || 0) + 1);
        while (pairs >= k) {
            ans += nums.length - right;
            freq.set(nums[left], freq.get(nums[left]) - 1);
            pairs -= freq.get(nums[left]);
            left++;
        }
    }
    return ans;
}
