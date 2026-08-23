// LeetCode 0779 - K-th Symbol in Grammar
// https://leetcode.com/problems/k-th-symbol-in-grammar/

/**
 * @param {number} n
 * @param {number} k
 * @return {number}
 */
var kthGrammar = function(n, k) {
    if (n === 1) return 0;
    const mid = 1 << (n - 2);
    if (k <= mid) return kthGrammar(n - 1, k);
    return 1 - kthGrammar(n - 1, k - mid);
};
