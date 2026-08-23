// LeetCode 2681 - Power of Heroes
// https://leetcode.com/problems/power-of-heroes/

var sumOfPower = function(nums) {
    const MOD = 1000000007;
    nums = nums.slice().sort((a, b) => a - b);
    let ans = 0, s = 0;
    for (const x of nums) {
        ans = (ans + ((s + x) % MOD) * x % MOD * x) % MOD;
        s = (s * 2 + x) % MOD;
    }
    return ans;
};
