// LeetCode 3079 - Find the Sum of Encrypted Integers
// https://leetcode.com/problems/find-the-sum-of-encrypted-integers/

export function sumOfEncryptedInt(nums: number[]): number {
    const encrypt = (x) => {
        let mx = 0, p = 0;
        for (; x > 0; x = Math.floor(x / 10)) {
            mx = Math.max(mx, x % 10);
            p = p * 10 + 1;
        }
        return mx * p;
    };
    let ans = 0;
    for (const x of nums) ans += encrypt(x);
    return ans;
}
