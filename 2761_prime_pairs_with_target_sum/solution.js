// LeetCode 2761 - Prime Pairs With Target Sum
// https://leetcode.com/problems/prime-pairs-with-target-sum/

/**
 * @param {number} n
 * @return {number[][]}
 */
var findPrimePairs = function(n) {
    const isPrime = Array(n + 1).fill(true);
    isPrime[0] = isPrime[1] = false;
    for (let i = 2; i * i <= n; i++) {
        if (isPrime[i]) {
            for (let j = i * i; j <= n; j += i) isPrime[j] = false;
        }
    }
    const ans = [];
    for (let x = 2; x <= n / 2; x++) {
        const y = n - x;
        if (isPrime[x] && isPrime[y]) ans.push([x, y]);
    }
    return ans;
};
