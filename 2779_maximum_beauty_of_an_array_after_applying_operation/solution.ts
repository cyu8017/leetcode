// LeetCode 2779 - Maximum Beauty of an Array After Applying Operation
// https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/

export function maximumBeauty(nums: number[], k: number): number {
    nums.sort((a, b) => a - b);
    let ans = 0, left = 0;
    for (let right = 0; right < nums.length; right++) {
        while (nums[right] - nums[left] > 2 * k) left++;
        ans = Math.max(ans, right - left + 1);
    }
    return ans;
}
