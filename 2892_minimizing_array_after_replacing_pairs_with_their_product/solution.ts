// LeetCode 2892 - Minimizing Array After Replacing Pairs With Their Product
// https://leetcode.com/problems/minimizing-array-after-replacing-pairs-with-their-product/

export function minArrayLength(nums: number[], k: number): number {
    if (nums.length === 0) return 0;
    let ans = 1;
    let prod = nums[0];
    for (let i = 1; i < nums.length; i++) {
        if (prod <= k && nums[i] <= k && (nums[i] === 0 || prod <= Math.floor(k / nums[i]))) {
            prod *= nums[i];
        } else {
            ans++;
            prod = nums[i];
        }
    }
    return ans;
}
