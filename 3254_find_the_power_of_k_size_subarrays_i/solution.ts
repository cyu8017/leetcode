// LeetCode 3254 - Find the Power of K-Size Subarrays I
// https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/

export function resultsArray(nums: any, k: any): any {
    const n = nums.length;
    const ans = new Array(n - k + 1);
    for (let i = 0; i <= n - k; i++) {
        let ok = true;
        for (let j = i + 1; j < i + k; j++) {
            if (nums[j] !== nums[j - 1] + 1) { ok = false; break; }
        }
        ans[i] = ok ? nums[i + k - 1] : -1;
    }
    return ans;
}
