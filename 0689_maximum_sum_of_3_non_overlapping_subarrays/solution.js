// LeetCode 0689 - Maximum Sum of 3 Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSumOfThreeSubarrays = function(nums, k) {
    const n = nums.length, windows = n - k + 1;
    const sums = new Array(windows).fill(0);
    let total = 0;
    for (let i = 0; i < k; i++) total += nums[i];
    sums[0] = total;
    for (let i = 1; i < windows; i++) {
        total += nums[i + k - 1] - nums[i - 1];
        sums[i] = total;
    }
    const left = new Array(windows).fill(0);
    let best = 0;
    for (let i = 0; i < windows; i++) {
        if (sums[i] > sums[best]) best = i;
        left[i] = best;
    }
    const right = new Array(windows).fill(0);
    best = windows - 1;
    for (let i = windows - 1; i >= 0; i--) {
        if (sums[i] >= sums[best]) best = i;
        right[i] = best;
    }
    let answer = [0, 0, 0];
    let bestTotal = -1;
    for (let mid = k; mid < windows - k; mid++) {
        const l = left[mid - k], r = right[mid + k];
        const cur = sums[l] + sums[mid] + sums[r];
        if (cur > bestTotal) {
            bestTotal = cur;
            answer = [l, mid, r];
        }
    }
    return answer;
};
