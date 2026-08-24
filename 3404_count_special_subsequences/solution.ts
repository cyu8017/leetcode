// LeetCode 3404 - Count Special Subsequences
// https://leetcode.com/problems/count-special-subsequences/

export function numberOfSubsequences(nums: any): any {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        for (let j = i + 2; j < n; j++) {
            for (let k = j + 2; k < n; k++) {
                for (let l = k + 2; l < n; l++) {
                    if (nums[i] * nums[k] === nums[j] * nums[l]) ans++;
                }
            }
        }
    }
    return ans;
}
