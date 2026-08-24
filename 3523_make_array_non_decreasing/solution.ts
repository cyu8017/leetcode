// LeetCode 3523 - Make Array Non-decreasing
// https://leetcode.com/problems/make-array-non-decreasing/

export function maximumPossibleSize(nums: any): any {
    let ans = 0, mx = 0;
    for (const x of nums) {
        if (mx <= x) {
            ans++;
            mx = x;
        }
    }
    return ans;
}
