// LeetCode 3770 - Largest Prime From Consecutive Prime Sum
// https://leetcode.com/problems/largest_prime_from_consecutive_prime_sum/

var largestPrime = function(n) {
    const MX = 500000;
    const isPrime = new Array(MX + 1).fill(true);
    isPrime[0] = isPrime[1] = false;
    const primes = [];
    for (let i = 2; i <= MX; i++) {
        if (isPrime[i]) {
            primes.push(i);
            if (i * i <= MX) {
                for (let j = i * i; j <= MX; j += i) isPrime[j] = false;
            }
        }
    }
    const S = [0];
    let t = 0;
    for (const x of primes) {
        t += x;
        if (t > MX) break;
        if (isPrime[t]) S.push(t);
    }
    let lo = 0, hi = S.length;
    while (lo < hi) {
        const mid = (lo + hi) >> 1;
        if (S[mid] <= n) lo = mid + 1;
        else hi = mid;
    }
    return S[lo - 1];
};
