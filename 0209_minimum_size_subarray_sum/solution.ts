// LeetCode 0209 - Minimum Size Subarray Sum
// https://leetcode.com/problems/minimum-size-subarray-sum/

export function minSubArrayLen(target: number, nums: number[]): number {
    let left = 0;
    let sum = 0;
    let best = Infinity;

    for (let right = 0; right < nums.length; right += 1) {
        sum += nums[right];
        while (sum >= target) {
            best = Math.min(best, right - left + 1);
            sum -= nums[left];
            left += 1;
        }
    }
    return best === Infinity ? 0 : best;
}