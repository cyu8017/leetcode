// LeetCode 0634 - Find the Derangement of An Array
// https://leetcode.com/problems/find-the-derangement-of-an-array/

/**
 * @param {number} n
 * @return {number}
 */
var findDerangement = function(n) {
    const mod = 1000000007;
    if (n === 1) return 0;
    let prev2 = 0, prev1 = 1;
    for (let size = 3; size <= n; ++size) {
        const next = ((size - 1) * (prev1 + prev2)) % mod;
        prev2 = prev1;
        prev1 = next;
    }
    return prev1;
};
