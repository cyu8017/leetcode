// LeetCode 1712 - Ways to Split Array Into Three Subarrays
// https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/

function waysToSplit(nums: number[]): number {
    const mod = 1000000007;
    const n = nums.length;
    const prefix: number[] = new Array(n);
    let total = 0;
    for (let i = 0; i < n; i++) {
        total += nums[i];
        prefix[i] = total;
    }

    const lowerBound = (target: number, lo: number, hi: number): number => {
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (prefix[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    };

    const upperBound = (target: number, lo: number, hi: number): number => {
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (prefix[mid] <= target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }
        return lo;
    };

    let ans = 0;
    for (let i = 0; i < n - 2; i++) {
        const left = prefix[i];
        const lo = lowerBound(2 * left, i + 1, n - 1);
        const hi = upperBound(Math.floor((total + left) / 2), lo, n - 1);
        ans = (ans + hi - lo) % mod;
    }
    return ans;
}
