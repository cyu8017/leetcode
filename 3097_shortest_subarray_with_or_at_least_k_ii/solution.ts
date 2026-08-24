// LeetCode 3097 - Shortest Subarray With OR at Least K II
// https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/

export function minimumSubarrayLength(nums: number[], k: number): number {
    const n = nums.length;
    const cnt = new Array(32).fill(0);
    let ans = n + 1, s = 0, i = 0;
    for (let j = 0; j < n; j++) {
        const x = nums[j];
        s |= x;
        for (let h = 0; h < 32; h++)
            if (((x >> h) & 1) !== 0) cnt[h]++;
        for (; s >= k && i <= j; i++) {
            ans = Math.min(ans, j - i + 1);
            for (let h = 0; h < 32; h++) {
                if (((nums[i] >> h) & 1) !== 0) {
                    cnt[h]--;
                    if (cnt[h] === 0) s ^= 1 << h;
                }
            }
        }
    }
    return ans === n + 1 ? -1 : ans;
}
