// LeetCode 2172 - Maximum AND Sum of Array
// https://leetcode.com/problems/maximum-and-sum-of-array/

export function maximumANDSum(nums: number[], numSlots: number): number {
    const n = nums.length, slots = numSlots;
    let maxMask = 1;
    for (let i = 0; i < slots; i++) maxMask *= 3;
    const dp = new Array(maxMask).fill(0);
    for (let mask = 0; mask < maxMask; mask++) {
        let cnt = 0, x = mask;
        while (x > 0) { cnt += x % 3; x = Math.floor(x / 3); }
        if (cnt >= n) continue;
        const v = nums[cnt];
        let bas = 1;
        for (let s = 1; s <= slots; s++) {
            const occ = Math.floor(mask / bas) % 3;
            if (occ < 2) {
                const nm = mask + bas;
                dp[nm] = Math.max(dp[nm], dp[mask] + (v & s));
            }
            bas *= 3;
        }
    }
    let best = 0;
    for (const v of dp) best = Math.max(best, v);
    return best;
}
