// LeetCode 0204 - Count Primes
// https://leetcode.com/problems/count-primes/

/**
 * @param {number} n
 * @return {number}
 */
var countPrimes = function(n) {
    if (n <= 2) return 0;

    const isPrime = new Array(n).fill(true);
    isPrime[0] = false;
    isPrime[1] = false;

    for (let p = 2; p * p < n; p += 1) {
        if (isPrime[p]) {
            for (let multiple = p * p; multiple < n; multiple += p) {
                isPrime[multiple] = false;
            }
        }
    }
    return isPrime.reduce((count, prime) => count + (prime ? 1 : 0), 0);
};