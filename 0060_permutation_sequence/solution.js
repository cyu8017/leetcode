// LeetCode 0060 - Permutation Sequence
// https://leetcode.com/problems/permutation-sequence/

/**
 * @param {number} n
 * @param {number} k
 * @return {string}
 */
var getPermutation = function(n, k) {
    const numbers = Array.from({ length: n }, (_, i) => i + 1);
    const factorials = new Array(n).fill(1);

    for (let i = 1; i < n; i++) {
        factorials[i] = factorials[i - 1] * i;
    }

    k -= 1;
    const result = [];

    for (let i = n - 1; i >= 0; i--) {
        const index = Math.floor(k / factorials[i]);
        result.push(String(numbers[index]));
        numbers.splice(index, 1);
        k %= factorials[i];
    }

    return result.join('');
};
