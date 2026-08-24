// LeetCode 2521 - Distinct Prime Factors of Product of Array
// https://leetcode.com/problems/distinct-prime-factors-of-product-of-array/

export function distinctPrimeFactors(nums: number[]): number {
    const set = new Set();
    for (let num of nums) {
        let x = num;
        for (let p = 2; p * p <= x; p++) {
            if (x % p === 0) {
                set.add(p);
                while (x % p === 0) x = Math.floor(x / p);
            }
        }
        if (x > 1) set.add(x);
    }
    return set.size;
}
