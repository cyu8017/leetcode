// LeetCode 1187 - Make Array Strictly Increasing
// https://leetcode.com/problems/make-array-strictly-increasing/

/**
 * @param {number[]} arr1
 * @param {number[]} arr2
 * @return {number}
 */
var makeArrayIncreasing = function(arr1, arr2) {
    arr2 = [...new Set(arr2)].sort((a, b) => a - b);
    let dp = new Map([[-1, 0]]);
    const bisectRight = (arr, x) => {
        let lo = 0, hi = arr.length;
        while (lo < hi) {
            const mid = (lo + hi) >> 1;
            if (arr[mid] <= x) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    };
    for (const num of arr1) {
        const next = new Map();
        for (const [prev, ops] of dp) {
            if (num > prev) {
                next.set(num, Math.min(next.get(num) ?? Infinity, ops));
            }
            const idx = bisectRight(arr2, prev);
            if (idx < arr2.length) {
                const chosen = arr2[idx];
                next.set(chosen, Math.min(next.get(chosen) ?? Infinity, ops + 1));
            }
        }
        dp = next;
        if (!dp.size) return -1;
    }
    return Math.min(...dp.values());
};
