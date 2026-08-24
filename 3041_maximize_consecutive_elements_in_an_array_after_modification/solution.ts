// LeetCode 3041 - Maximize Consecutive Elements in an Array After Modification
// https://leetcode.com/problems/maximize-consecutive-elements-in-an-array-after-modification/

export function maxSelectedElements(nums: any): any {
    nums.sort((a, b) => a - b);
    const dp = new Map();
    let ans = 0;
    for (const num of nums) {
        const dn = dp.get(num) || 0;
        const dnm1 = dp.get(num - 1) || 0;
        dp.set(num + 1, dn + 1);
        dp.set(num, dnm1 + 1);
        ans = Math.max(ans, Math.max(dp.get(num), dp.get(num + 1)));
    }
    return ans;
}
