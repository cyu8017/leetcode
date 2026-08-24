// LeetCode 2875 - Minimum Size Subarray in Infinite Array
// https://leetcode.com/problems/minimum-size-subarray-in-infinite-array/

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var minSizeSubarray = function(nums, target) {
    const n = nums.length;
    let total = 0;
    for (const v of nums) total += v;
    let ans = 1 << 30;
    if (total > 0) {
        const loops = Math.floor(target / total);
        const remain = target % total;
        if (remain === 0) return loops * n;
        const arr = nums.concat(nums);
        let left = 0, sum = 0, best = 1 << 30;
        for (let right = 0; right < arr.length; right++) {
            sum += arr[right];
            while (sum > remain && left <= right) {
                sum -= arr[left];
                left++;
            }
            if (sum === remain && right - left + 1 < best) best = right - left + 1;
        }
        if (best < (1 << 30)) ans = loops * n + best;
    }
    return ans === (1 << 30) ? -1 : ans;
};
