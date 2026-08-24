// LeetCode 3176 - Find the Maximum Length of a Good Subsequence I
// https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-i/

export function maximumLength(nums: any, k: any): any {
    const n = nums.length;
    const f = Array.from({length: n}, () => new Array(k + 1).fill(0));
    let ans = 0;
    for (let i = 0; i < n; i++) {
        for (let h = 0; h <= k; h++) {
            for (let j = 0; j < i; j++) {
                if (nums[i] === nums[j]) f[i][h] = Math.max(f[i][h], f[j][h]);
                else if (h > 0) f[i][h] = Math.max(f[i][h], f[j][h - 1]);
            }
            f[i][h]++;
        }
        ans = Math.max(ans, f[i][k]);
    }
    return ans;
}
