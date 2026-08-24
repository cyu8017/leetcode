// LeetCode 2524 - Maximum Frequency Score of a Subarray
// https://leetcode.com/problems/maximum-frequency-score-of-a-subarray/

export function maxFrequencyScore(nums: number[], k: number): number {
    const MOD = 1000000007;
    const modPow = (a, e) => {
        let res = 1;
        a %= MOD;
        while (e > 0) {
            if (e & 1) res = res * a % MOD;
            a = a * a % MOD;
            e >>= 1;
        }
        return res;
    };
    const freq = new Map();
    const add = (score, x) => {
        const c = freq.get(x) || 0;
        if (c > 0) score = (score - modPow(x, c) + MOD) % MOD;
        freq.set(x, c + 1);
        return (score + modPow(x, c + 1)) % MOD;
    };
    const remove = (score, x) => {
        const c = freq.get(x);
        score = (score - modPow(x, c) + MOD) % MOD;
        if (c === 1) freq.delete(x);
        else {
            freq.set(x, c - 1);
            score = (score + modPow(x, c - 1)) % MOD;
        }
        return score;
    };
    let score = 0, best = 0;
    for (let i = 0; i < nums.length; i++) {
        score = add(score, nums[i]);
        if (i >= k) score = remove(score, nums[i - k]);
        if (i >= k - 1 && score > best) best = score;
    }
    return best;
}
