// LeetCode 3231 - Minimum Number of Increasing Subsequence to Be Removed
// https://leetcode.com/problems/minimum-number-of-increasing-subsequence-to-be-removed/

export function minOperations(nums: any): any {
    const g = [];
    for (const x of nums) {
        let l = 0, r = g.length;
        while (l < r) {
            const mid = (l + r) >> 1;
            if (g[mid] < x) r = mid;
            else l = mid + 1;
        }
        if (l === g.length) g.push(x);
        else g[l] = x;
    }
    return g.length;
}
