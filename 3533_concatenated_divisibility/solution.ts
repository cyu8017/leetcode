// LeetCode 3533 - Concatenated Divisibility
// https://leetcode.com/problems/concatenated-divisibility/

export function concatenatedDivisibility(nums: any, k: any): any {
    nums = nums.slice().sort((a, b) => a - b);
    const n = nums.length;
    const pows = new Array(n);
    for (let i = 0; i < n; i++) {
        let p = 1, num = nums[i];
        if (num === 0) p = 10 % k;
        else {
            for (let x = num; x > 0; x = Math.floor(x / 10)) p = p * 10 % k;
        }
        pows[i] = p;
    }
    const memo = new Map();
    function dp(mask: any, mod: any): any {
        if (mask === (1 << n) - 1) return mod === 0;
        const key = (BigInt(mask) << 32n) | BigInt(mod);
        if (memo.has(key)) return memo.get(key);
        for (let i = 0; i < n; i++) {
            if (((mask >> i) & 1) === 0) {
                const nm = (mod * pows[i] + nums[i]) % k;
                if (dp(mask | (1 << i), nm)) {
                    memo.set(key, true);
                    return true;
                }
            }
        }
        memo.set(key, false);
        return false;
    }    function reconstruct(mask: any, mod: any): any {
        for (let i = 0; i < n; i++) {
            if (((mask >> i) & 1) === 0) {
                const nm = (mod * pows[i] + nums[i]) % k;
                if (dp(mask | (1 << i), nm)) {
                    const rest = reconstruct(mask | (1 << i), nm);
                    rest.unshift(nums[i]);
                    return rest;
                }
            }
        }
        return [];
    }    if (!dp(0, 0)) return [];
    return reconstruct(0, 0);
}
