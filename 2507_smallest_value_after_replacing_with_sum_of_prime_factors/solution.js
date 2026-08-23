// LeetCode 2507 - Smallest Value After Replacing With Sum of Prime Factors
// https://leetcode.com/problems/smallest-value-after-replacing-with-sum-of-prime-factors/

/**
 * @param {number} n
 * @return {number}
 */
var smallestValue = function(n) {
    const sumPrimeFactors = (x) => {
        let s = 0;
        for (let i = 2; i * i <= x; i++) {
            while (x % i === 0) {
                s += i;
                x = Math.floor(x / i);
            }
        }
        if (x > 1) s += x;
        return s;
    };
    while (true) {
        const s = sumPrimeFactors(n);
        if (s === n) return n;
        n = s;
    }
};
