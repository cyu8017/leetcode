// LeetCode 2523 - Closest Prime Numbers in Range
// https://leetcode.com/problems/closest-prime-numbers-in-range/

/**
 * @param {number} left
 * @param {number} right
 * @return {number[]}
 */
var closestPrimes = function(left, right) {
    const isPrime = new Array(right + 1).fill(true);
    if (right >= 0) isPrime[0] = false;
    if (right >= 1) isPrime[1] = false;
    for (let i = 2; i * i <= right; i++) {
        if (!isPrime[i]) continue;
        for (let j = i * i; j <= right; j += i) isPrime[j] = false;
    }
    const primes = [];
    for (let i = left; i <= right; i++) if (isPrime[i]) primes.push(i);
    if (primes.length < 2) return [-1, -1];
    let bestDiff = Infinity, best = [-1, -1];
    for (let i = 0; i + 1 < primes.length; i++) {
        const d = primes[i + 1] - primes[i];
        if (d < bestDiff) {
            bestDiff = d;
            best = [primes[i], primes[i + 1]];
        }
    }
    return best;
};
