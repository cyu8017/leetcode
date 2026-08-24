// LeetCode 3247 - Number of Subsequences with Odd Sum
// https://leetcode.com/problems/number-of-subsequences-with-odd-sum/

export function subsequenceCount(nums: any): any {
    const mod = 1000000007;
    let f = [0, 0];
    for (const x of nums) {
        const g = [0, 0];
        if (x % 2 === 1) {
            g[0] = (f[0] + f[1]) % mod;
            g[1] = (f[0] + f[1] + 1) % mod;
        } else {
            g[0] = (f[0] + f[0] + 1) % mod;
            g[1] = (f[1] + f[1]) % mod;
        }
        f = g;
    }
    return f[1];
}
