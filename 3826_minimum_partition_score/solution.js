// LeetCode 3826 - Minimum Partition Score
// https://leetcode.com/problems/minimum_partition_score/

var minPartitionScore = function(nums, k) {
    const n = nums.length;
    const INF = Number.MAX_SAFE_INTEGER / 4;
    const prefix = new Array(n + 1).fill(0);
    for (let i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
    let previous = new Array(n + 1).fill(INF);
    previous[0] = 0;
    const value = (left, right) => {
        const sum = prefix[right] - prefix[left];
        return sum * (sum + 1) / 2;
    };
    let current;
    const compute = (lo, hi, optLo, optHi) => {
        if (lo > hi) return;
        const mid = (lo + hi) >> 1;
        let bestIndex = -1;
        const end = Math.min(optHi, mid - 1);
        for (let split = optLo; split <= end; split++) {
            if (previous[split] === INF) continue;
            const candidate = previous[split] + value(split, mid);
            if (candidate < current[mid]) {
                current[mid] = candidate;
                bestIndex = split;
            }
        }
        if (bestIndex === -1) bestIndex = optLo;
        compute(lo, mid - 1, optLo, bestIndex);
        compute(mid + 1, hi, bestIndex, optHi);
    };
    for (let parts = 1; parts <= k; parts++) {
        current = new Array(n + 1).fill(INF);
        compute(parts, n, parts - 1, n - 1);
        previous = current;
    }
    return previous[n];
};
