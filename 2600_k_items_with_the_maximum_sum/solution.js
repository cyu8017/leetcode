// LeetCode 2600 - K Items With the Maximum Sum
// https://leetcode.com/problems/k-items-with-the-maximum-sum/

/**
 * @param {number} numOnes
 * @param {number} numZeros
 * @param {number} numNegOnes
 * @param {number} k
 * @return {number}
 */
var kItemsWithMaximumSum = function(numOnes, numZeros, numNegOnes, k) {
    let ans = 0;
    let take = Math.min(numOnes, k);
    ans += take;
    k -= take;
    take = Math.min(numZeros, k);
    k -= take;
    take = Math.min(numNegOnes, k);
    ans -= take;
    return ans;
};
