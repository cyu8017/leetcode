// LeetCode 3233 - Find the Count of Numbers Which Are Not Special
// https://leetcode.com/problems/find-the-count-of-numbers-which-are-not-special/

var nonSpecialCount = function(l, r) {
    const M = 31623;
    if (!nonSpecialCount._primes) {
        const primes = new Array(M + 1).fill(true);
        primes[0] = primes[1] = false;
        for (let i = 2; i <= M; i++) {
            if (primes[i]) {
                for (let j = i * 2; j <= M; j += i) primes[j] = false;
            }
        }
        nonSpecialCount._primes = primes;
    }
    const primes = nonSpecialCount._primes;
    const lo = Math.ceil(Math.sqrt(l));
    const hi = Math.floor(Math.sqrt(r));
    let cnt = 0;
    for (let i = lo; i <= hi; i++) if (primes[i]) cnt++;
    return r - l + 1 - cnt;
};
