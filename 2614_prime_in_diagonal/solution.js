// LeetCode 2614 - Prime In Diagonal
// https://leetcode.com/problems/prime-in-diagonal/

/**
 * @param {number[][]} nums
 * @return {number}
 */
var diagonalPrime = function(nums) {
    const isPrime = (x) => {
        if (x < 2) return false;
        for (let i = 2; i * i <= x; ++i) if (x % i === 0) return false;
        return true;
    };
    const n = nums.length;
    let best = 0;
    for (let i = 0; i < n; ++i) {
        const a = nums[i][i], b = nums[i][n - 1 - i];
        if (isPrime(a) && a > best) best = a;
        if (isPrime(b) && b > best) best = b;
    }
    return best;
};
