// LeetCode 3801 - Minimum Cost To Merge Sorted Lists
// https://leetcode.com/problems/minimum_cost_to_merge_sorted_lists/

var minMergeCost = function(lists) {
    const m = lists.length;
    const totalMasks = 1 << m;
    const merged = Array.from({length: totalMasks}, () => []);
    const length = new Array(totalMasks).fill(0);
    const median = new Array(totalMasks).fill(0);
    const trailingZeros = (bit) => {
        let n = 0;
        while ((bit & 1) === 0) { bit >>= 1; n++; }
        return n;
    };
    for (let mask = 1; mask < totalMasks; mask++) {
        const bit = mask & -mask;
        const index = trailingZeros(bit);
        const previous = merged[mask ^ bit];
        const current = lists[index];
        const out = [];
        let i = 0, j = 0;
        while (i < previous.length || j < current.length) {
            if (j === current.length || (i < previous.length && previous[i] <= current[j])) {
                out.push(previous[i++]);
            } else {
                out.push(current[j++]);
            }
        }
        merged[mask] = out;
        length[mask] = out.length;
        median[mask] = out[Math.floor((out.length - 1) / 2)];
    }
    const INF = Number.MAX_SAFE_INTEGER;
    const dp = new Array(totalMasks).fill(0);
    for (let mask = 1; mask < totalMasks; mask++) {
        if ((mask & (mask - 1)) === 0) continue;
        dp[mask] = INF;
        const firstBit = mask & -mask;
        for (let left = (mask - 1) & mask; left > 0; left = (left - 1) & mask) {
            if ((left & firstBit) === 0) continue;
            const right = mask ^ left;
            if (right === 0) continue;
            let diff = median[left] - median[right];
            if (diff < 0) diff = -diff;
            const candidate = dp[left] + dp[right] + length[mask] + diff;
            if (candidate < dp[mask]) dp[mask] = candidate;
        }
    }
    return dp[totalMasks - 1];
};
