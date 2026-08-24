// LeetCode 2731 - Movement of Robots
// https://leetcode.com/problems/movement-of-robots/

export function sumDistance(nums: number[], s: string, d: number): number {
    const MOD = 1000000007;
    const n = nums.length;
    const pos = new Array(n);
    for (let i = 0; i < n; i++) pos[i] = nums[i] + (s[i] === 'R' ? d : -d);
    pos.sort((a, b) => a - b);
    let ans = 0, pref = 0;
    for (let i = 0; i < n; i++) {
        ans = (ans + ((pos[i] * i - pref) % MOD + MOD) % MOD) % MOD;
        pref += pos[i];
    }
    return (ans % MOD + MOD) % MOD;
}
