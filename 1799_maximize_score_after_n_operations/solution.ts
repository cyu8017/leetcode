// LeetCode 1799 - Maximize Score After N Operations
// https://leetcode.com/problems/maximize-score-after-n-operations/

function maxScore(nums: number[]): number {
    const n = nums.length;
    const full = (1 << n) - 1;
    const memo = new Map<number, number>();

    const gcd = (a: number, b: number): number => {
        while (b !== 0) {
            [a, b] = [b, a % b];
        }
        return a;
    };
    const popcount = (x: number): number => {
        let count = 0;
        while (x) {
            x &= x - 1;
            count++;
        }
        return count;
    };

    const dp = (mask: number): number => {
        if (mask === full) return 0;
        const cached = memo.get(mask);
        if (cached !== undefined) return cached;
        const step = (popcount(mask) >> 1) + 1;
        let best = 0;
        for (let i = 0; i < n; i++) {
            if ((mask >> i) & 1) continue;
            for (let j = i + 1; j < n; j++) {
                if ((mask >> j) & 1) continue;
                best = Math.max(
                    best,
                    step * gcd(nums[i], nums[j]) + dp(mask | (1 << i) | (1 << j))
                );
            }
        }
        memo.set(mask, best);
        return best;
    };

    return dp(0);
}
