// LeetCode 2670 - Find the Distinct Difference Array
// https://leetcode.com/problems/find-the-distinct-difference-array/

export function distinctDifferenceArray(nums: any): any {
    const n = nums.length;
    const suf = new Array(n + 1).fill(0);
    const seen = new Set();
    for (let i = n - 1; i >= 0; i--) {
        seen.add(nums[i]);
        suf[i] = seen.size;
    }
    seen.clear();
    const ans = new Array(n);
    for (let i = 0; i < n; i++) {
        seen.add(nums[i]);
        ans[i] = seen.size - suf[i + 1];
    }
    return ans;
}
