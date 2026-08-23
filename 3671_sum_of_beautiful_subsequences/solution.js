// LeetCode 3671 - Sum of Beautiful Subsequences
// https://leetcode.com/problems/sum-of-beautiful-subsequences/

var totalBeauty = function(nums) {
    const MOD = 1000000007;
    let mx = 0;
    for (const v of nums) if (v > mx) mx = v;
    const pos = Array.from({length: mx + 1}, () => []);
    for (let i = 0; i < nums.length; i++) pos[nums[i]].push(i);
    const cnt = new Array(mx + 1).fill(0);
    for (let g = 1; g <= mx; g++) {
        const seq = [];
        for (let m = g; m <= mx; m += g) seq.push(...pos[m]);
        if (seq.length === 0) continue;
        seq.sort((a, b) => a - b);
        let ways = 1;
        for (let i = 0; i < seq.length; i++) ways = (ways * 2) % MOD;
        cnt[g] = (ways - 1 + MOD) % MOD;
    }
    let ans = 0;
    for (let g = mx; g >= 1; g--) {
        for (let m = 2 * g; m <= mx; m += g)
            cnt[g] = (cnt[g] - cnt[m] + MOD) % MOD;
        ans = (ans + cnt[g] * g) % MOD;
    }
    return ans;
};
