// LeetCode 3509 - Maximum Product of Subsequences With an Alternating Sum Equal to K
// https://leetcode.com/problems/maximum-product-of-subsequences-with-an-alternating-sum-equal-to-k/

export function maxProduct(nums: any, k: any, limit: any): any {
    const MIN = -5000;
    const memo = new Map();
    let sumAll = 0;
    for (const v of nums) sumAll += v;
    if (Math.abs(k) > sumAll) return -1;
    function dp(i: any, product: any, state: any, kk: any): any {
        if (i === nums.length) {
            if (kk === 0 && state !== 0 && product <= limit) return product;
            return MIN;
        }
        const key = i + ',' + product + ',' + state + ',' + kk;
        if (memo.has(key)) return memo.get(key);
        let res = dp(i + 1, product, state, kk);
        if (state === 0) res = Math.max(res, dp(i + 1, nums[i], 1, kk - nums[i]));
        if (state === 1) {
            let np = product * nums[i];
            if (np > limit + 1) np = limit + 1;
            res = Math.max(res, dp(i + 1, np, 2, kk + nums[i]));
        }
        if (state === 2) {
            let np = product * nums[i];
            if (np > limit + 1) np = limit + 1;
            res = Math.max(res, dp(i + 1, np, 1, kk - nums[i]));
        }
        memo.set(key, res);
        return res;
    }    const ans = dp(0, 1, 0, k);
    return ans === MIN ? -1 : ans;
}
