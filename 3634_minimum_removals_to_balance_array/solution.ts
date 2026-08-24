// LeetCode 3634 - Minimum Removals to Balance Array
// https://leetcode.com/problems/minimum-removals-to-balance-array/

export function minRemoval(nums: any, k: any): any {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const lowerBound = (a, target) => {
        let lo = 0, hi = a.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (a[mid] < target) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    let cnt = 0;
    for (let i = 0; i < n; i++) {
        let j = n;
        if (nums[i] * k <= nums[n - 1]) {
            const target = nums[i] * k + 1;
            j = lowerBound(nums, target);
        }
        cnt = Math.max(cnt, j - i);
    }
    return n - cnt;
}
