// LeetCode 3868 - Minimum Cost To Equalize Arrays Using Swaps
// https://leetcode.com/problems/minimum-cost-to-equalize-arrays-using-swaps/

export function minCost(nums1: any, nums2: any): any {
    const cnt2 = new Map();
    for (const x of nums2) cnt2.set(x, (cnt2.get(x) || 0) + 1);
    const cnt1 = new Map();
    for (const x of nums1) {
        const c = cnt2.get(x) || 0;
        if (c > 0) cnt2.set(x, c - 1);
        else cnt1.set(x, (cnt1.get(x) || 0) + 1);
    }
    let ans = 0;
    for (const v of cnt1.values()) {
        if (v % 2 === 1) return -1;
        ans += Math.floor(v / 2);
    }
    for (const v of cnt2.values()) {
        if (v % 2 === 1) return -1;
    }
    return ans;
}
