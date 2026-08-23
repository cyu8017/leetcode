// LeetCode 0325 - Maximum Size Subarray Sum Equals k
var maxSubArrayLen = function(nums, k) {
    const prefixIndex = new Map([[0, -1]]);
    let prefix = 0;
    let best = 0;
    for (let index = 0; index < nums.length; index += 1) {
        prefix += nums[index];
        if (prefixIndex.has(prefix - k)) best = Math.max(best, index - prefixIndex.get(prefix - k));
        if (!prefixIndex.has(prefix)) prefixIndex.set(prefix, index);
    }
    return best;
};
