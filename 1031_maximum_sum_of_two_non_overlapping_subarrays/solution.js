// LeetCode 1031 - Maximum Sum of Two Non-Overlapping Subarrays
// https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/

/**
 * @param {number[]} nums
 * @param {number} firstLen
 * @param {number} secondLen
 * @return {number}
 */
var maxSumTwoNoOverlap = function(nums, firstLen, secondLen) {
    const prefix = [0];
    for (const x of nums) prefix.push(prefix[prefix.length - 1] + x);
    const best = (a, b) => {
        let bestA = 0, ans = 0;
        for (let i = a + b; i < prefix.length; i++) {
            bestA = Math.max(bestA, prefix[i - b] - prefix[i - b - a]);
            ans = Math.max(ans, bestA + prefix[i] - prefix[i - b]);
        }
        return ans;
    };
    return Math.max(best(firstLen, secondLen), best(secondLen, firstLen));
};
