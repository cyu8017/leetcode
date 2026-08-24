// LeetCode 2470 - Number of Subarrays With LCM Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-lcm-equal-to-k/

export function subarrayLCM(nums: number[], k: number): number {
    const gcd = (a, b) => {
        while (b !== 0) {
            const t = a % b;
            a = b;
            b = t;
        }
        return a;
    };
    let ans = 0;
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        let cur = 1;
        for (let j = i; j < n; j++) {
            cur = Math.floor(cur / gcd(cur, nums[j])) * nums[j];
            if (cur > k) break;
            if (cur === k) ans++;
        }
    }
    return ans;
}
