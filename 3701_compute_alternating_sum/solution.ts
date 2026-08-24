// LeetCode 3701 - Compute Alternating Sum
// https://leetcode.com/problems/compute-alternating-sum/

export function alternatingSum(nums: any): any {
    let ans = 0;
    for (let i = 0; i < nums.length; i++) {
        if (i % 2 === 0) ans += nums[i];
        else ans -= nums[i];
    }
    return ans;
}
