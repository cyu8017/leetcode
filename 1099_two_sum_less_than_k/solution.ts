// LeetCode 1099 - Two Sum Less Than K
// https://leetcode.com/problems/two-sum-less-than-k/

function twoSumLessThanK(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);
    let lo = 0;
    let hi = nums.length - 1;
    let ans = -1;
    while (lo < hi) {
        const total = nums[lo] + nums[hi];
        if (total < k) {
            ans = Math.max(ans, total);
            lo++;
        } else {
            hi--;
        }
    }
    return ans;
}
