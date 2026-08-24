// LeetCode 3314 - Construct the Minimum Bitwise Array I
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-i/

export function minBitwiseArray(nums: any): any {
    const ans = new Array(nums.length).fill(-1);
    for (let i = 0; i < nums.length; i++) {
        const n = nums[i];
        for (let x = 0; x < n; x++) {
            if ((x | (x + 1)) === n) { ans[i] = x; break; }
        }
    }
    return ans;
}
