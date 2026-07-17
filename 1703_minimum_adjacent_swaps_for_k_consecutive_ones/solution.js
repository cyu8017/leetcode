// LeetCode 1703 - Minimum Adjacent Swaps for K Consecutive Ones
// https://leetcode.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var minMoves = function(nums, k) {
    const adjusted = [];
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            adjusted.push(i - adjusted.length);
        }
    }
    const prefix = [0];
    for (const value of adjusted) {
        prefix.push(prefix[prefix.length - 1] + value);
    }
    let best = Infinity;
    for (let left = 0; left + k <= adjusted.length; left++) {
        const right = left + k;
        const mid = left + Math.floor(k / 2);
        const median = adjusted[mid];
        let cost = median * (mid - left) - (prefix[mid] - prefix[left]);
        cost += (prefix[right] - prefix[mid + 1]) - median * (right - mid - 1);
        best = Math.min(best, cost);
    }
    return best;
};
