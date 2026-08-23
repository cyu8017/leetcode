// LeetCode 2597 - The Number of Beautiful Subsets
// https://leetcode.com/problems/the-number-of-beautiful-subsets/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var beautifulSubsets = function(nums, k) {
    const freq = new Map();
    for (const x of nums) freq.set(x, (freq.get(x) || 0) + 1);
    const groups = new Map();
    for (const key of freq.keys()) {
        const rem = key % k;
        if (!groups.has(rem)) groups.set(rem, []);
        groups.get(rem).push(key);
    }
    let ans = 1;
    for (const vals of groups.values()) {
        vals.sort((a, b) => a - b);
        let prevTake = 0, prevSkip = 1;
        let prevVal = -Infinity;
        for (const v of vals) {
            let ways = 1;
            for (let i = 0; i < freq.get(v); ++i) ways *= 2;
            ways--;
            const skip = prevTake + prevSkip;
            let take = ways * prevSkip;
            if (prevVal + k !== v) take += ways * prevTake;
            prevTake = take;
            prevSkip = skip;
            prevVal = v;
        }
        ans *= prevTake + prevSkip;
    }
    return ans - 1;
};
