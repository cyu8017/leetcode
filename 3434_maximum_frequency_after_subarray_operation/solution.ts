// LeetCode 3434 - Maximum Frequency After Subarray Operation
// https://leetcode.com/problems/maximum-frequency-after-subarray-operation/

export function maxFrequency(nums: any, k: any): any {
    let base = 0;
    for (const x of nums) if (x === k) base++;
    let ans = base;
    const uniq = new Set(nums);
    for (const v of uniq) {
        if (v === k) continue;
        let best = 0, cur = 0;
        for (const x of nums) {
            let delta = 0;
            if (x === v) delta = 1;
            else if (x === k) delta = -1;
            cur += delta;
            if (cur < 0) cur = 0;
            if (cur > best) best = cur;
        }
        if (base + best > ans) ans = base + best;
    }
    return ans;
}
