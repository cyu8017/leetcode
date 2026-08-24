// LeetCode 2447 - Number of Subarrays With GCD Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

export function subarrayGCD(nums: number[], k: number): number {
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
        let g = 0;
        for (let j = i; j < n; j++) {
            g = gcd(g, nums[j]);
            if (g < k) break;
            if (g === k) ans++;
        }
    }
    return ans;
}
