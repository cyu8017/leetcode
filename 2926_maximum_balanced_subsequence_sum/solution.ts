// LeetCode 2926 - Maximum Balanced Subsequence Sum
// https://leetcode.com/problems/maximum-balanced-subsequence-sum/

export function maxBalancedSubsequenceSum(nums: number[]): number {
    const NEG_INF = Number.MIN_SAFE_INTEGER / 4;
    const n = nums.length;
    const keys = nums.map((v, i) => v - i);
    const uniq = [...new Set(keys)].sort((a, b) => a - b);
    const bit = Array(uniq.length + 2).fill(NEG_INF);
    const idxOf = (v) => {
        let lo = 0, hi = uniq.length;
        while (lo < hi) {
            const mid = (lo + hi) >>> 1;
            if (uniq[mid] < v) lo = mid + 1;
            else hi = mid;
        }
        return lo + 1;
    };
    const update = (i, val) => {
        for (; i < bit.length; i += i & -i)
            if (val > bit[i]) bit[i] = val;
    };
    const query = (i) => {
        let best = NEG_INF;
        for (; i > 0; i -= i & -i)
            if (bit[i] > best) best = bit[i];
        return best;
    };
    let ans = NEG_INF;
    for (let i = 0; i < n; i++) {
        const id = idxOf(keys[i]);
        const best = query(id);
        let cur = nums[i];
        if (best > NEG_INF / 2) {
            const cand = best + nums[i];
            if (cand > cur) cur = cand;
        }
        update(id, cur);
        if (cur > ans) ans = cur;
    }
    return ans;
}
