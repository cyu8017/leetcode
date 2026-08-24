// LeetCode 2702 - Minimum Operations to Make Numbers Non-positive
// https://leetcode.com/problems/minimum-operations-to-make-numbers-non-positive/

export function minOperations(nums: any, x: any, y: any): any {
    let lo = 0, hi = 0;
    for (const v of nums) {
        hi = Math.max(hi, Math.ceil(v / y));
        hi = Math.max(hi, Math.ceil(v / x));
    }
    hi += nums.length;
    const ok = (ops) => {
        let extra = 0;
        for (const v of nums) {
            const remain = v - ops * y;
            if (remain > 0) extra += Math.ceil(remain / (x - y));
        }
        return extra <= ops;
    };
    while (lo < hi) {
        const mid = Math.floor((lo + hi) / 2);
        if (ok(mid)) hi = mid;
        else lo = mid + 1;
    }
    return lo;
}
