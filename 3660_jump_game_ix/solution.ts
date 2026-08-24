// LeetCode 3660 - Jump Game IX
// https://leetcode.com/problems/jump-game-ix/

export function maxValue(nums: any): any {
    const n = nums.length;
    const ans = new Array(n);
    const preMax = new Array(n);
    preMax[0] = nums[0];
    for (let i = 1; i < n; i++) preMax[i] = Math.max(preMax[i - 1], nums[i]);
    let sufMin = 1073741823;
    for (let i = n - 1; i >= 0; i--) {
        if (preMax[i] > sufMin) ans[i] = ans[i + 1];
        else ans[i] = preMax[i];
        sufMin = Math.min(sufMin, nums[i]);
    }
    return ans;
}
