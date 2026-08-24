// LeetCode 0713 - Subarray Product Less Than K
// https://leetcode.com/problems/subarray-product-less-than-k/

export function numSubarrayProductLessThanK(nums: number[], k: number): number {
    if (k <= 1) return 0;
    let product = 1, left = 0, ans = 0;
    for (let right = 0; right < nums.length; right++) {
        product *= nums[right];
        while (product >= k) product = Math.floor(product / nums[left++]);
        ans += right - left + 1;
    }
    return ans;
}
