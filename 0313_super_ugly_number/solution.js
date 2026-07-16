// LeetCode 0313 - Super Ugly Number
// https://leetcode.com/problems/super-ugly-number/

/**
 * @param {number} n
 * @param {number[]} primes
 * @return {number}
 */
var nthSuperUglyNumber = function(n, primes) {
    const ugly = [1];
    const pointers = Array(primes.length).fill(0);
    while (ugly.length < n) {
        const nextValues = primes.map((prime, index) => ugly[pointers[index]] * prime);
        const nextUgly = Math.min(...nextValues);
        ugly.push(nextUgly);
        for (let index = 0; index < primes.length; index += 1) {
            if (nextUgly === ugly[pointers[index]] * primes[index]) {
                pointers[index] += 1;
            }
        }
    }
    return ugly[ugly.length - 1];
};
