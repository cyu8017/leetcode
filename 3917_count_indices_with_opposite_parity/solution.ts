// LeetCode 3917 - Count Indices With Opposite Parity
// https://leetcode.com/problems/count-indices-with-opposite-parity/

export function countOppositeParity(nums: any): any {
    const cnt = [0, 0];
    for (const x of nums) cnt[x & 1]++;
    const n = nums.length;
    const ans = new Array(n);
    for (let i = 0; i < n; i++) {
        const x = nums[i];
        cnt[x & 1]--;
        ans[i] = cnt[(x & 1) ^ 1];
    }
    return ans;
}
