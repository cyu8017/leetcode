// LeetCode 0762 - Prime Number of Set Bits in Binary Representation
// https://leetcode.com/problems/prime-number-of-set-bits-in-binary-representation/

/**
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var countPrimeSetBits = function(left, right) {
    const primes = new Set([2, 3, 5, 7, 11, 13, 17, 19]);
    let ans = 0;
    for (let num = left; num <= right; num++) {
        let bits = 0, x = num;
        while (x > 0) { bits += x & 1; x >>>= 1; }
        if (primes.has(bits)) ans++;
    }
    return ans;
};
