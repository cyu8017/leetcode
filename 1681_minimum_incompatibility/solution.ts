// LeetCode 1681 - Minimum Incompatibility
// https://leetcode.com/problems/minimum-incompatibility/

function bitCount1681(x: number): number {
    let c = 0;
    while (x) {
        x &= x - 1;
        c++;
    }
    return c;
}

function minimumIncompatibility(nums: number[], k: number): number {
    const n = nums.length;
    const size = n / k;
    const full = (1 << n) - 1;
    const groups = new Map<number, number>();
    for (let mask = 0; mask < (1 << n); mask++) {
        if (bitCount1681(mask) !== size) continue;
        const vals: number[] = [];
        for (let i = 0; i < n; i++) if ((mask >> i) & 1) vals.push(nums[i]);
        if (new Set(vals).size === size) groups.set(mask, Math.max(...vals) - Math.min(...vals));
    }
    const memo = new Map<number, number>();
    const dp = (mask: number): number => {
        if (mask === full) return 0;
        if (memo.has(mask)) return memo.get(mask)!;
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
}
