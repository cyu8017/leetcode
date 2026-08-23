// LeetCode 1852 - Distinct Numbers in Each Subarray
// https://leetcode.com/problems/distinct-numbers-in-each-subarray/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var distinctNumbers = function(nums, k) {
    const counts = new Map();
    for (let i = 0; i < k; i++) {
        counts.set(nums[i], (counts.get(nums[i]) || 0) + 1);
    }
    const result = [counts.size];
    let left = 0;
    for (let right = k; right < nums.length; right++) {
        counts.set(nums[right], (counts.get(nums[right]) || 0) + 1);
        const outgoing = nums[left++];
        const next = counts.get(outgoing) - 1;
        if (next === 0) counts.delete(outgoing);
        else counts.set(outgoing, next);
        result.push(counts.size);
    }
    return result;
};
