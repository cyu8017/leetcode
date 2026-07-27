// LeetCode 1681 - Minimum Incompatibility
// https://leetcode.com/problems/minimum-incompatibility/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minimumIncompatibility = function(nums, k) {
    const n = nums.length;
    const size = n / k;
    const full = (1 << n) - 1;
    const groups = new Map();
    for (let mask = 0; mask < (1 << n); mask++) {
        if (bitCount(mask) !== size) continue;
        const vals = [];
        for (let i = 0; i < n; i++) if ((mask >> i) & 1) vals.push(nums[i]);
        if (new Set(vals).size === size) groups.set(mask, Math.max(...vals) - Math.min(...vals));
    }
    const memo = new Map();
    const dp = (mask) => {
        if (mask === full) return 0;
        if (memo.has(mask)) return memo.get(mask);
        let first = 0;
        while ((mask >> first) & 1) first++;
        let best = 1e9;
        for (const [g, c] of groups) {
            if (((g >> first) & 1) && !(g & mask)) best = Math.min(best, c + dp(mask | g));
        }
        memo.set(mask, best);
        return best;
    };
    const ans = dp(0);
    return ans >= 1e9 ? -1 : ans;
};

function bitCount(x) {
    let c = 0;
    while (x) {
        x &= x - 1;
        c++;
    }
    return c;
}
