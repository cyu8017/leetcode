// LeetCode 3852 - Smallest Pair With Different Frequencies
// https://leetcode.com/problems/smallest-pair-with-different-frequencies/

var minDistinctFreqPair = function(nums) {
    const cnt = new Map();
    for (const v of nums) cnt.set(v, (cnt.get(v) || 0) + 1);
    let x = nums[0];
    for (const v of nums) x = Math.min(x, v);
    let minY = Infinity;
    for (const y of cnt.keys()) {
        if (y < minY && cnt.get(x) !== cnt.get(y)) minY = y;
    }
    if (minY === Infinity) return [-1, -1];
    return [x, minY];
};
