// LeetCode 3312 - Sorted GCD Pair Queries
// https://leetcode.com/problems/sorted-gcd-pair-queries/

var gcdValues = function(nums, queries) {
    let maxV = 0;
    for (const x of nums) if (x > maxV) maxV = x;
    const cnt = new Array(maxV + 1).fill(0);
    for (const x of nums) cnt[x]++;
    const divCnt = new Array(maxV + 1).fill(0);
    for (let g = 1; g <= maxV; g++) {
        let c = 0;
        for (let m = g; m <= maxV; m += g) c += cnt[m];
        divCnt[g] = c * (c - 1) / 2;
    }
    const exact = new Array(maxV + 1).fill(0);
    for (let g = maxV; g >= 1; g--) {
        exact[g] = divCnt[g];
        for (let m = 2 * g; m <= maxV; m += g) exact[g] -= exact[m];
    }
    const pref = new Array(maxV + 1).fill(0);
    for (let g = 1; g <= maxV; g++) pref[g] = pref[g - 1] + exact[g];
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const q = queries[i];
        let lo = 1, hi = maxV;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (pref[mid] > q) hi = mid;
            else lo = mid + 1;
        }
        ans[i] = lo;
    }
    return ans;
};
