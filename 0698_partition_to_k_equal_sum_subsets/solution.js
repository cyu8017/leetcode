// LeetCode 0698 - Partition to K Equal Sum Subsets
// https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var canPartitionKSubsets = function(nums, k) {
    let total = 0;
    for (const x of nums) total += x;
    if (total % k !== 0) return false;
    const target = Math.floor(total / k);
    const arr = nums.slice().sort((a, b) => a - b).reverse();
    if (arr[0] > target) return false;
    const buckets = new Array(k).fill(0);
    const dfs = (index) => {
        if (index === arr.length) return true;
        for (let i = 0; i < buckets.length; i++) {
            if (buckets[i] + arr[index] > target) continue;
            buckets[i] += arr[index];
            if (dfs(index + 1)) return true;
            buckets[i] -= arr[index];
            if (buckets[i] === 0) break;
        }
        return false;
    };
    return dfs(0);
};
