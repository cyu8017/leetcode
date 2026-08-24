// LeetCode 3315 - Construct the Minimum Bitwise Array II
// https://leetcode.com/problems/construct-the-minimum-bitwise-array-ii/

export function minBitwiseArray(nums: any): any {
    const ans = new Array(nums.length).fill(-1);
    for (let i = 0; i < nums.length; i++) {
        const n = nums[i];
        if (n === 2) continue;
        for (let b = 0; b < 31; b++) {
            if (((n >> b) & 1) === 0) continue;
            const x = n ^ (1 << b);
            if ((x | (x + 1)) === n) { ans[i] = x; break; }
        }
    }
    return ans;
}
