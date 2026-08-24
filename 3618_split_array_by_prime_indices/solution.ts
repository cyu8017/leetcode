// LeetCode 3618 - Split Array by Prime Indices
// https://leetcode.com/problems/split-array-by-prime-indices/

export function splitArray(nums: any): any {
    const M = 100010;
    if (!splitArray._primes) {
        const primes = new Array(M).fill(true);
        primes[0] = primes[1] = false;
        for (let i = 2; i < M; i++)
            if (primes[i])
                for (let j = i + i; j < M; j += i) primes[j] = false;
        splitArray._primes = primes;
    }
    const pr = splitArray._primes;
    let ans = 0;
    for (let i = 0; i < nums.length; i++) {
        if (pr[i]) ans += nums[i];
        else ans -= nums[i];
    }
    return Math.abs(ans);
}
