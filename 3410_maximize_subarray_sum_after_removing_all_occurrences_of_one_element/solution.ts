// LeetCode 3410 - Maximize Subarray Sum After Removing All Occurrences of One Element
// https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/

export function maxSubarraySum(nums: any): any {
    const kadane = (a) => {
        let best = Number.MIN_SAFE_INTEGER, cur = 0;
        for (const x of a) {
            cur += x;
            if (cur > best) best = cur;
            if (cur < 0) cur = 0;
        }
        let allNeg = true;
        let mx = a[0];
        for (const x of a) {
            if (x > mx) mx = x;
            if (x >= 0) allNeg = false;
        }
        if (allNeg) return mx;
        return best;
    };
    let ans = kadane(nums);
    const uniq = new Set();
    for (const x of nums) if (x < 0) uniq.add(x);
    for (const v of uniq) {
        const b = [];
        for (const x of nums) if (x !== v) b.push(x);
        if (b.length === 0) continue;
        const cand = kadane(b);
        if (cand > ans) ans = cand;
    }
    return ans;
}
