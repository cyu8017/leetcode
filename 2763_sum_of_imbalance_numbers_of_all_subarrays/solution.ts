// LeetCode 2763 - Sum of Imbalance Numbers of All Subarrays
// https://leetcode.com/problems/sum-of-imbalance-numbers-of-all-subarrays/

export function sumImbalanceNumbers(nums: number[]): number {
    const n = nums.length;
    let ans = 0;
    for (let i = 0; i < n; i++) {
        const seen = new Set();
        const sorted = [];
        let imbalance = 0;
        const ceilIdx = (x) => {
            let lo = 0, hi = sorted.length;
            while (lo < hi) {
                const mid = (lo + hi) >> 1;
                if (sorted[mid] < x) lo = mid + 1;
                else hi = mid;
            }
            return lo;
        };
        for (let j = i; j < n; j++) {
            const x = nums[j];
            if (!seen.has(x)) {
                seen.add(x);
                const idx = ceilIdx(x);
                const next = idx < sorted.length ? sorted[idx] : null;
                const prev = idx > 0 ? sorted[idx - 1] : null;
                if (prev !== null && x - prev !== 1) imbalance++;
                if (next !== null && next - x !== 1) imbalance++;
                if (prev !== null && next !== null && next - prev > 1) imbalance--;
                sorted.splice(idx, 0, x);
            }
            ans += imbalance;
        }
    }
    return ans;
}
